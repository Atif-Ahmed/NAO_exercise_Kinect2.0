import time

import dialog_nao as dialog
import exercise_poses as ex_pos
import exercise_tracking as track
import speech_module as speech


def start(_posture):
    _posture.goToPosture("StandInit", 1.0)
    speech.speak(dialog.start_exercise_2)
    speech.speak(dialog.exercise_2_how_to)
    _posture.goToPosture("Stand", 2.0)
    speech.speak(dialog.follow_me)

    # *********************************************************************************
    # ************************ SET ONE  - Front - Side ********************************
    speech.speak(dialog.one, wait=False)
    ex_pos.left_front()
    speech.speak(dialog.two, wait=False)
    ex_pos.right_front()
    result = track.track_pose(track.pose['Left_Front'], track.pose['Right_Front'], 2)
    print(result)

    speech.speak(dialog.three, wait=False)
    ex_pos.left_side()
    speech.speak(dialog.four, wait=False)
    ex_pos.right_side()
    result = track.track_pose(track.pose['Left_Side'], track.pose['Right_Side'], 2)
    print(result)

    speech.speak(dialog.relax, wait=False)
    ex_pos.left_down()
    ex_pos.right_down()
    time.sleep(2)

    speech.speak(dialog.one, wait=False)
    ex_pos.left_front()
    speech.speak(dialog.two, wait=False)
    ex_pos.right_front()
    result = track.track_pose(track.pose['Left_Front'], track.pose['Right_Front'], 2)
    print(result)

    speech.speak(dialog.three, wait=False)
    ex_pos.left_side()
    speech.speak(dialog.four, wait=False)
    ex_pos.right_side()
    result = track.track_pose(track.pose['Left_Side'], track.pose['Right_Side'], 2)
    print(result)

    speech.speak(dialog.relax, wait=False)
    ex_pos.left_down()
    ex_pos.right_down()
    time.sleep(4)
    speech.speak(dialog.okay_next)
    # *********************************************************************************
    # *********************************************************************************

    # *********************************************************************************
    # ************************ SET TWO  - Up - Side ***********************************

    speech.speak(dialog.one, wait=False)
    ex_pos.left_side()
    speech.speak(dialog.two, wait=False)
    ex_pos.right_side()
    result = track.track_pose(track.pose['Left_Side'], track.pose['Right_Side'], 2)
    print(result)

    speech.speak(dialog.three, wait=False)
    ex_pos.left_up()
    speech.speak(dialog.four, wait=False)
    ex_pos.right_up()
    result = track.track_pose(track.pose['Left_Up'], track.pose['Right_Up'], 2)
    print(result)

    speech.speak(dialog.relax, wait=False)
    ex_pos.left_down()
    ex_pos.right_down()
    time.sleep(2)

    speech.speak(dialog.one, wait=False)
    ex_pos.left_side()
    speech.speak(dialog.two, wait=False)
    ex_pos.right_side()
    result = track.track_pose(track.pose['Left_Side'], track.pose['Right_Side'], 2)
    print(result)


    speech.speak(dialog.three, wait=False)
    ex_pos.left_up()
    speech.speak(dialog.four, wait=False)
    ex_pos.right_up()
    result = track.track_pose(track.pose['Left_Up'], track.pose['Right_Up'], 2)
    print(result)

    speech.speak(dialog.relax, wait=False)
    ex_pos.left_down()
    ex_pos.right_down()
    time.sleep(4)
    speech.speak(dialog.okay_next)
    # *********************************************************************************
    # *********************************************************************************

    # *********************************************************************************
    # ************************ SET THREE  - Up - BendUp *********************************

    speech.speak(dialog.one, wait=False)
    ex_pos.left_bend_up()
    speech.speak(dialog.two, wait=False)
    ex_pos.right_bend_up()
    result = track.track_pose(track.pose['Left_BendUp'], track.pose['Right_BendUp'], 2)
    print(result)

    speech.speak(dialog.three, wait=False)
    ex_pos.left_up()
    speech.speak(dialog.four, wait=False)
    ex_pos.right_up()
    result = track.track_pose(track.pose['Left_Up'], track.pose['Right_Up'], 2)
    print(result)

    speech.speak(dialog.one, wait=False)
    ex_pos.left_bend_up()
    speech.speak(dialog.two, wait=False)
    ex_pos.right_bend_up()
    result = track.track_pose(track.pose['Left_BendUp'], track.pose['Right_BendUp'], 2)
    print(result)

    speech.speak(dialog.three, wait=False)
    ex_pos.left_up()
    speech.speak(dialog.four, wait=False)
    ex_pos.right_up()
    result = track.track_pose(track.pose['Left_Up'], track.pose['Right_Up'], 2)
    print(result)

    speech.speak(dialog.relax, wait=False)
    ex_pos.left_down()
    ex_pos.right_down()
    time.sleep(4)
    # *********************************************************************************
    # *********************************************************************************

    # *********************************************************************************
    # ************************ SET FOUR  - Side  - Front *******************
    # speech.speak(dialog.one, wait=False)
    # ex_pos.left_front()
    # speech.speak(dialog.two, wait=False)
    # ex_pos.right_front()
    # result = track.track_pose(track.pose['Left_Front'], track.pose['Right_Front'], 2, False)
    # print(result)
    # speech.speak(dialog.three, wait=False)
    # ex_pos.left_side()
    # speech.speak(dialog.four, wait=False)
    # ex_pos.right_side()
    # result = track.track_pose(track.pose['Left_Side'], track.pose['Right_Side'], 2)
    # print(result)
    #
    # speech.speak(dialog.relax, wait=False)
    # ex_pos.left_down()
    # ex_pos.right_down()
    # time.sleep(2)
    #
    # speech.speak(dialog.one, wait=False)
    # ex_pos.left_front()
    # speech.speak(dialog.two, wait=False)
    # ex_pos.right_front()
    # result = track.track_pose(track.pose['Left_Front'], track.pose['Right_Front'], 2, False)
    # print(result)
    # speech.speak(dialog.three, wait=False)
    # ex_pos.left_side()
    # speech.speak(dialog.four, wait=False)
    # ex_pos.right_side()
    # result = track.track_pose(track.pose['Left_Side'], track.pose['Right_Side'], 2)
    # print(result)
    #
    # speech.speak(dialog.one, wait=False)
    # ex_pos.left_front()
    # speech.speak(dialog.two, wait=False)
    # ex_pos.right_front()
    # result = track.track_pose(track.pose['Left_Front'], track.pose['Right_Front'], 2, False)
    # print(result)
    # speech.speak(dialog.three, wait=False)
    # ex_pos.left_side()
    # speech.speak(dialog.four, wait=False)
    # ex_pos.right_side()
    # result = track.track_pose(track.pose['Left_Side'], track.pose['Right_Side'], 2)
    # print(result)
    #
    # speech.speak(dialog.relax, wait=False)
    # ex_pos.left_down()
    # ex_pos.right_down()
    # time.sleep(4)

    # *********************************************************************************
    # *********************************************************************************

    speech.speak(dialog.end_exercise_2)
    speech.speak(dialog.relax_long)

    time.sleep(3)
    # *********************************************************************************
    # *********************************************************************************
