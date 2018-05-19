import ctypes

import numpy
import pygame as window
from pykinect2 import PyKinectV2
from pykinect2 import PyKinectRuntime
from pygame.locals import *
import users

import arm_tracking

WINDOW_SIZE = 1920,  1080
red = window.color.THECOLORS['red']

# Global variables
screen = None  # handle to Kinect video window (pygame Window)
screen_cpy = None #copy of screen buffer
device = None  # handle to Kinect device
skeleton = None  # Tuple of skeleton data 3D
is_tracked = False #is the body being tracked
arm_length = None  # data to store information of _right_arm
frame_surface = None # draw surface for pygame
enable_video = True  # enable disable video feed
prevHeadLocation = None  # location of previous head position in 3D space

# initialize Kinect device
# noinspection PyUnresolvedReferences,PyUnboundLocalVariable
def init():
    # Initialize variable at global level
    global screen, device, frame_surface
    # Initialize PyGame
    window.init()
    infoObject = window.display.Info()
    screen = window.display.set_mode((infoObject.current_w >> 1, infoObject.current_h >> 1), window.HWSURFACE | window.DOUBLEBUF | window.RESIZABLE, 32)
    window.display.set_caption("Kinect for Windows v2 Body Game")

    screen.fill(window.color.THECOLORS["black"])
    device = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color | PyKinectV2.FrameSourceTypes_Body)
    frame_surface = window.Surface((device.color_frame_desc.Width, device.color_frame_desc.Height), 0, 32)

def get_skeleton(bodies):
    global skeleton, device, is_tracked, prevHeadLocation

    skeleton_2_d = []
    skeleton = None
    skeleton_list = []
    joints_list = []
    is_tracked_list =[]
    is_tracked = False
    for i in range(0, device.max_body_count):
        body = bodies.bodies[i]
        if not body.is_tracked:
            continue

        joints = body.joints
        joints_list.append(joints)
        joints_array = []
        is_tracked = True
        for j in range(0, PyKinectV2.JointType_Count):
            position = joints[j].Position
            # if not tracked set to zero..
            if  joints[j].TrackingState == PyKinectV2.TrackingState_NotTracked:
                is_tracked = False
                position.x = 0.0
                position.y = 0.0
                position.z = 0.0

            joints_array.append(position)
        skeleton_list.append(joints_array)
        is_tracked_list.append(is_tracked)

    if(len(skeleton_list)>0):
        if prevHeadLocation == None:
            skeleton = skeleton_list[0]
            is_tracked = is_tracked_list[0]
            skeleton_2_d = device.body_joints_to_color_space(joints_list[0])
            prevHeadLocation = skeleton[PyKinectV2.JointType_Head].z
            return skeleton_2D_array(skeleton_2_d)

        else:

            if(len(skeleton_list) == 1):
                skeleton = skeleton_list[0]
                is_tracked = is_tracked_list[0]
                skeleton_2_d = device.body_joints_to_color_space(joints_list[0])
                prevHeadLocation = skeleton[PyKinectV2.JointType_Head].z
                return skeleton_2D_array(skeleton_2_d)
                ##print(skeleton[PyKinectV2.JointType_Head].z)

            minDist = 10000
            if (len(skeleton_list) > 1):
                # find the head closest to the previous head location
                print(len(skeleton_list), " Different peoples are being tracked.")
                final_index = -1
                for sk_i in range(0, len(skeleton_list)):
                    tempSkeleton = skeleton_list[sk_i]
                    tempHead =  tempSkeleton[PyKinectV2.JointType_Head].z
                    if(minDist > numpy.abs(tempHead - prevHeadLocation)):
                        minDist = numpy.abs(tempHead - prevHeadLocation)
                        final_index = sk_i
                skeleton = skeleton_list[final_index]
                prevHeadLocation = skeleton[PyKinectV2.JointType_Head].z
                # convert joint coordinates to color space
                skeleton_2_d = device.body_joints_to_color_space(joints_list[final_index])
                is_tracked = is_tracked_list[final_index]
                return skeleton_2D_array(skeleton_2_d)

    return None

def draw_skeleton(_skeleton):
    # draw Circles for joints
    window.draw.circle(frame_surface, red, map(int, _skeleton[PyKinectV2.JointType_Head]), 10)
    window.draw.circle(frame_surface, red, map(int, _skeleton[PyKinectV2.JointType_SpineMid]), 10)
    window.draw.circle(frame_surface, red, map(int, _skeleton[PyKinectV2.JointType_SpineShoulder]), 10)
    window.draw.circle(frame_surface, red, map(int, _skeleton[PyKinectV2.JointType_ShoulderRight]), 10)
    window.draw.circle(frame_surface, red, map(int, _skeleton[PyKinectV2.JointType_ElbowRight]), 10)
    window.draw.circle(frame_surface, red, map(int, _skeleton[PyKinectV2.JointType_WristRight]), 10)
    window.draw.circle(frame_surface, red, map(int, _skeleton[PyKinectV2.JointType_HandRight]), 10)
    window.draw.circle(frame_surface, red, map(int, _skeleton[PyKinectV2.JointType_ShoulderLeft]), 10)
    window.draw.circle(frame_surface, red, map(int, _skeleton[PyKinectV2.JointType_ElbowLeft]), 10)
    window.draw.circle(frame_surface, red, map(int, _skeleton[PyKinectV2.JointType_WristLeft]), 10)
    window.draw.circle(frame_surface, red, map(int, _skeleton[PyKinectV2.JointType_HandLeft]), 10)
# Draw lines on All connections
    window.draw.line(frame_surface, red, map(int, _skeleton[PyKinectV2.JointType_Head]), map(int, _skeleton[PyKinectV2.JointType_SpineShoulder]), 2)
    window.draw.line(frame_surface, red, map(int, _skeleton[PyKinectV2.JointType_SpineMid]), map(int, _skeleton[PyKinectV2.JointType_SpineShoulder]), 2)
    window.draw.line(frame_surface, red, map(int, _skeleton[PyKinectV2.JointType_SpineMid]), map(int, _skeleton[PyKinectV2.JointType_SpineBase]), 2)

# Right Arm
    window.draw.line(frame_surface, red, map(int, _skeleton[PyKinectV2.JointType_SpineShoulder]), map(int, _skeleton[PyKinectV2.JointType_ShoulderRight]), 2)
    window.draw.line(frame_surface, red, map(int, _skeleton[PyKinectV2.JointType_ShoulderRight]), map(int, _skeleton[PyKinectV2.JointType_ElbowRight]), 2)
    window.draw.line(frame_surface, red, map(int, _skeleton[PyKinectV2.JointType_ElbowRight]), map(int, _skeleton[PyKinectV2.JointType_WristRight]), 2)
    window.draw.line(frame_surface, red, map(int, _skeleton[PyKinectV2.JointType_WristRight]), map(int, _skeleton[PyKinectV2.JointType_HandRight]), 2)

    # Left Arm
    window.draw.line(frame_surface, red, map(int, _skeleton[PyKinectV2.JointType_SpineShoulder]), map(int, _skeleton[PyKinectV2.JointType_ShoulderLeft]), 2)
    window.draw.line(frame_surface, red, map(int, _skeleton[PyKinectV2.JointType_ShoulderLeft]), map(int, _skeleton[PyKinectV2.JointType_ElbowLeft]), 2)
    window.draw.line(frame_surface, red, map(int, _skeleton[PyKinectV2.JointType_ElbowLeft]), map(int, _skeleton[PyKinectV2.JointType_WristLeft]), 2)
    window.draw.line(frame_surface, red, map(int, _skeleton[PyKinectV2.JointType_WristLeft]), map(int, _skeleton[PyKinectV2.JointType_HandLeft]), 2)
    # Shoulder to Shoulder

    window.draw.line(frame_surface, red, map(int, _skeleton[PyKinectV2.JointType_ShoulderRight]), map(int, _skeleton[PyKinectV2.JointType_ShoulderLeft]), 2)

def device_angle_up():
    device.camera.elevation_angle += 2
    print "Device Camera Angle = ", device.camera.elevation_angle

def device_angle_down():
    device.camera.elevation_angle -= 2
    print "Device Camera Angle = ", device.camera.elevation_angle

def draw_angles():
    """Fetch the angle information from arm analysis and draw it on screen"""
    my_font = window.font.SysFont("Arial", size=45)

    # Left Shoulder Angle display
    text = "Left Should Angle: %s" % arm_tracking.shoulder_left_angle
    frame_surface.blit(my_font.render(str(text), True, (0, 0, 0)), (10, WINDOW_SIZE[1] - 60))

    # Right Shoulder Angle display
    text = "Right Should Angle: %s" % arm_tracking.shoulder_right_angle
    frame_surface.blit(my_font.render(str(text), True, (0, 0, 0)), (10, WINDOW_SIZE[1] - 90))

    # Left Elbow Angle display
    text = "Left Elbow Angle: %s" % arm_tracking.elbow_left_angle
    frame_surface.blit(my_font.render(str(text), True, (0, 0, 0)), (10, WINDOW_SIZE[1] - 120))

    # Right Elbow Angle display
    text = "Right Elbow Angle: %s" % arm_tracking.elbow_right_angle
    frame_surface.blit(my_font.render(str(text), True, (0, 0, 0)), (10, WINDOW_SIZE[1] - 150))

def draw_score():
    my_font = window.font.SysFont("Arial", size=45)
    text = "Score: %s" % int(users.get_total_score())
    frame_surface.blit(my_font.render(str(text), True, (0, 0, 0)), (30, 30))

# Kinect V2 draw Color Frame
def draw_color_frame(frame, target_surface):
    global device
    target_surface.lock()
    address = device.surface_as_array(target_surface.get_buffer())
    ctypes.memmove(address, frame.ctypes.data, frame.size)
    del address
    target_surface.unlock()

def skeleton_2D_array(_skeleton):
    skeleton_array = [];
    for i in range(0, _skeleton.size):
        if(_skeleton[i].x == float('-inf') or _skeleton[i].x == float('inf') or
                   _skeleton[i].y == float('-inf') or _skeleton[i].y == float('inf')):
            skeleton_array.append([0, 0])
        else:
            skeleton_array.append([_skeleton[i].x,_skeleton[i].y])
    return skeleton_array