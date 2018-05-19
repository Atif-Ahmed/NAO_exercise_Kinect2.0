import random
import time

import dialog_nao as dialog
import exercise_poses as ex_pos
import exercise_tracking as track
import speech_module as speech

pose_list_left = {0: [ex_pos.left_front, 'Left_Front'],
                  1: [ex_pos.left_up, 'Left_Up'],
                  2: [ex_pos.left_side, 'Left_Side'],
                  3: [ex_pos.left_bend_front, 'Left_BendFront'],
                  4: [ex_pos.left_bend_up, 'Left_BendUp']
                  }

pose_list_right = {0: [ex_pos.right_front, 'Right_Front'],
                   1: [ex_pos.right_up, 'Right_Up'],
                   2: [ex_pos.right_side, 'Right_Side'],
                   3: [ex_pos.right_bend_front, 'Right_BendFront'],
                   4: [ex_pos.right_bend_up, 'Right_BendUp']
                   }


def start(_posture):
    _posture.goToPosture("StandInit", 1.0)
    speech.speak(dialog.start_exercise_3)
    speech.speak(dialog.exercise_3_how_to)
    _posture.goToPosture("Stand", 2.0)
    speech.speak(dialog.exercise_3_repeat1)

    # *********************************************************************************
    # ************************ SET ONE  -  ********************************************
    move_count = 1
    prev_num = -1000
    left = []
    right = []

    for i in range(0, move_count):
        num = random.randint(0, 4)
        while num == prev_num:
            num = random.randint(0, 4)
        prev_num = num
        left.append(pose_list_left[num])
        right.append(pose_list_right[num])

    for i in range(0, move_count):
        left[i][0]()
        right[i][0]()
        time.sleep(1)

    speech.speak(dialog.exercise_3_repeat2)
    for i in range(0, move_count):
        result = track.track_pose(track.pose[left[i][1]], track.pose[right[i][1]], 3, False)
    print(result)
    if result:
        speech.speak(dialog.positive_feedback[random.randint(0, (len(dialog.positive_feedback) - 1))])
    else:
        speech.speak(dialog.encouraging_feedback[random.randint(0, (len(dialog.encouraging_feedback) - 1))])
    speech.speak(dialog.relax, wait=False)
    ex_pos.left_down()
    ex_pos.right_down()
    time.sleep(2)
    speech.speak(dialog.okay_next)

    # *********************************************************************************
    # ************************ SET TWO  -  ********************************************
    move_count = 1
    prev_num = -1000
    left = []
    right = []

    for i in range(0, move_count):
        num = random.randint(0, 4)
        while num == prev_num:
            num = random.randint(0, 4)
        prev_num = num
        left.append(pose_list_left[num])
        right.append(pose_list_right[num])

    for i in range(0, move_count):
        left[i][0]()
        right[i][0]()
        time.sleep(1)

    speech.speak(dialog.exercise_3_repeat2)
    for i in range(0, move_count):
        result = track.track_pose(track.pose[left[i][1]], track.pose[right[i][1]], 3, False)
    print(result)
    if result:
        speech.speak(dialog.positive_feedback[random.randint(0, (len(dialog.positive_feedback) - 1))])
    else:
        speech.speak(dialog.encouraging_feedback[random.randint(0, (len(dialog.encouraging_feedback) - 1))])

    speech.speak(dialog.relax, wait=False)
    ex_pos.left_down()
    ex_pos.right_down()
    time.sleep(2)
    speech.speak(dialog.okay_next)

    # *********************************************************************************
    # ************************ SET THREE  -  ********************************************
    move_count = 1
    prev_num = -1000
    left = []
    right = []

    for i in range(0, move_count):
        num = random.randint(0, 4)
        while num == prev_num:
            num = random.randint(0, 4)
        prev_num = num
        left.append(pose_list_left[num])
        right.append(pose_list_right[num])

    for i in range(0, move_count):
        left[i][0]()
        right[i][0]()
        time.sleep(1)

    speech.speak(dialog.exercise_3_repeat2)
    for i in range(0, move_count):
        result = track.track_pose(track.pose[left[i][1]], track.pose[right[i][1]], 3, False)
    print(result)
    if result:
        speech.speak(dialog.positive_feedback[random.randint(0, (len(dialog.positive_feedback) - 1))])
    else:
        speech.speak(dialog.encouraging_feedback[random.randint(0, (len(dialog.encouraging_feedback) - 1))])

    speech.speak(dialog.relax, wait=False)
    ex_pos.left_down()
    ex_pos.right_down()
    time.sleep(2)
    speech.speak(dialog.okay_next)

    # *********************************************************************************
    # *********************************************************************************

    speech.speak(dialog.end_exercise_3)
    time.sleep(3)
    # *********************************************************************************
    # *********************************************************************************
