import time

import dialog_nao as dialog
import exercise_poses as ex_pos
import exercise_tracking as track
import speech_module as speech


def start(_posture):
    _posture.goToPosture("StandInit", 1.0)
    speech.speak(dialog.start_exercise_session)
    speech.speak(dialog.start_exercise_1)
    speech.speak(dialog.exercise_1_how_to)
    _posture.goToPosture("Stand", 2.0)
    speech.speak(dialog.follow_me)

    # 1 *********************************************************************************
    ex_pos.left_front()
    ex_pos.right_front()
    result = track.track_pose(track.pose['Left_Front'], track.pose['Right_Front'], 1)
    print(result)

    speech.speak(dialog.relax, wait=False)
    ex_pos.left_down()
    ex_pos.right_down()
    time.sleep(2)

    # 2 *********************************************************************************
    ex_pos.left_side()
    ex_pos.right_side()
    result = track.track_pose(track.pose['Left_Side'], track.pose['Right_Side'], 1)
    print(result)

    speech.speak(dialog.relax, wait=False)
    ex_pos.left_down()
    ex_pos.right_down()
    time.sleep(2)

    # 3 *********************************************************************************
    ex_pos.left_up()
    ex_pos.right_up()
    result = track.track_pose(track.pose['Left_Up'], track.pose['Right_Up'], 1)
    print(result)

    speech.speak(dialog.relax, wait=False)
    ex_pos.left_down()
    ex_pos.right_down()
    time.sleep(2)

    # 4 *********************************************************************************
    ex_pos.left_bend_up()
    ex_pos.right_bend_up()
    result = track.track_pose(track.pose['Left_BendUp'], track.pose['Right_BendUp'], 1)
    print(result)

    speech.speak(dialog.relax, wait=False)
    ex_pos.left_down()
    ex_pos.right_down()
    time.sleep(2)

    # 5 *********************************************************************************
    ex_pos.left_up()
    ex_pos.right_up()
    result = track.track_pose(track.pose['Left_Up'], track.pose['Right_Up'], 1)
    print(result)

    speech.speak(dialog.relax, wait=False)
    ex_pos.left_down()
    ex_pos.right_down()
    time.sleep(2)

    # 6 *********************************************************************************
    ex_pos.left_bend_front()
    ex_pos.right_bend_front()
    result = track.track_pose(track.pose['Left_BendFront'], track.pose['Right_BendFront'], 1)
    print(result)

    # *********************************************************************************
    # *********************************************************************************
    speech.speak(dialog.relax, wait=False)
    ex_pos.left_down()
    ex_pos.right_down()
    time.sleep(2)

    speech.speak(dialog.end_exercise_1)
    speech.speak(dialog.relax_long)

    time.sleep(3)

