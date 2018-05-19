from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime

import ctypes
import _ctypes



import pygame
import sys
import users
import time
import dialog_nao as dialog
import kinect_interface as kinect
import nao_interface as nao
import speech_module as speech
import webbrowser
from threading import Thread
import arm_tracking
import Exercise.exercise_tracking as ex_tracking

# colors for drawing different bodies
SKELETON_COLORS = [pygame.color.THECOLORS["red"],
                   pygame.color.THECOLORS["blue"],
                   pygame.color.THECOLORS["green"],
                   pygame.color.THECOLORS["orange"],
                   pygame.color.THECOLORS["purple"],
                   pygame.color.THECOLORS["yellow"],
                   pygame.color.THECOLORS["violet"]]

loop = None
newFrame = False

def game_loop():
    global loop

    bodies = None

    loop = True
    kinect.init()
    while loop:

        events = kinect.window.event.get()
        for event in events:
            if event.type == kinect.window.QUIT:
                loop = False

            if event.type == kinect.window.VIDEORESIZE:  # window resized
                kinect.window.display.set_mode(event.dict['size'],
                                                       kinect.window.HWSURFACE | kinect.window.DOUBLEBUF | kinect.window.RESIZABLE, 32)

            if event.type == kinect.window.KEYDOWN:
                if event.key == kinect.window.K_UP:
                    kinect.device_angle_up()
                if event.key == kinect.window.K_DOWN:
                    kinect.device_angle_down()
                if event.key == kinect.window.K_g:
                    kinect.arm_tracking.display_graph()

        if kinect.device.has_new_color_frame():
            frame = kinect.device.get_last_color_frame()
            kinect.draw_color_frame(frame, kinect.frame_surface)
            kinect.screen_cpy = kinect.window.Surface.copy(kinect.frame_surface)
            kinect.screen_cpy = pygame.transform.scale(kinect.screen_cpy, (848, 480))
            frame = None

        # --- Cool! We have a body frame, so can get skeletons
        if kinect.device.has_new_body_frame():
            bodies = kinect.device.get_last_body_frame()

        # --- draw skeletons to _frame_surface
        if bodies is not None:
            skeleton_2_d = kinect.get_skeleton(bodies)
            if skeleton_2_d is not None:
                kinect.draw_skeleton(skeleton_2_d)
                arm_tracking.compute_angles(kinect.skeleton)
                kinect.draw_angles()
                kinect.draw_score()
                if ex_tracking.is_Tracking:
                    users.record_user_state()
                if ex_tracking.is_identify:
                    ex_tracking.get_arm_locations(kinect.skeleton)
        # --- copy back buffer surface pixels to the screen, resize it if needed and keep aspect ratio
        # --- (screen size may be different from Kinect's color frame size)
        h_to_w = float(kinect.frame_surface.get_height()) / kinect.frame_surface.get_width()
        target_height = int(h_to_w * kinect.screen.get_width())
        surface_to_draw = pygame.transform.scale(kinect.frame_surface, (kinect.screen.get_width(), target_height))
        kinect.screen.blit(surface_to_draw, (0, 0))
        surface_to_draw = None
        pygame.display.update()

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()


def main():
    # create user account in database or ask for login
    users.login_screen()

    if not users.userData:
        sys.exit()

    # initialize actual robot or virtual robot
    is_simulated = True
    nao.init(is_simulated)
    speech.init(is_simulated)

    # initialize the Kinect for Skeleton Tracking and video on a separate thread
    thread_kinect = Thread(target=game_loop)
    thread_kinect.start()
    time.sleep(4)

    nao.posture.goToPosture("Stand", 1.0)
    speech.speak(dialog.welcome)
    speech.speak(dialog.welcome_wait)

    ex_tracking.init()
    # Wait for the user calibration process to complete
    while kinect.skeleton is None:
        pass
    time.sleep(3)

    # TODO write the logic to wait for session to start when user is ready

    #create folder for user and session.
    users.create_user_folder();

    # starting the exercise session....
    nao.start_session()

    # save data of user
    users.save_stat_db()

    # user feedback form
    speech.speak(dialog.fill_in_form_1)
    speech.speak(dialog.fill_in_form_2)
    speech.speak(dialog.fill_in_form_3)
    speech.speak(dialog.bye)
    webbrowser.open('https://docs.google.com/forms/d/e/1FAIpQLSdN6wpiVMCAks6rIIB7U5g18vbaoO0-j_YBO2CeqEl5nEH7bg/viewform')

    # Exit the program

    thread_kinect.join()


if __name__ == "__main__":
    main()
