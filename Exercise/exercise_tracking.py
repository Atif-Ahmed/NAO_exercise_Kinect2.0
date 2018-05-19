import random
import time

import arm_tracking as arm
import dialog_nao as dialog
import speech_module as speech
import users
import pickle
import skfuzzy as fuzz
import numpy as np
from pykinect2 import PyKinectV2

#############################################################################################
#                               NFS Identification -- BEGIN
#############################################################################################

left_neural_net = []
left_fuzzy_sets = []
left_fuzzy_sets_range = []
right_neural_net = []
right_fuzzy_sets = []
right_fuzzy_sets_range = []
arm_pos_cartesian = []

is_identify = False

time_for_step = 12.0
count = 1
is_Tracking = False


def init():
    global right_neural_net, right_fuzzy_sets, right_fuzzy_sets_range
    global left_neural_net, left_fuzzy_sets, left_fuzzy_sets_range
    with open('Exercise/Trained/Left_Arm_NN.pickle', 'r') as f:
        [left_neural_net, left_fuzzy_sets, left_fuzzy_sets_range] = pickle.load(f)
        f.close()

    with open('Exercise/Trained/Right_Arm_NN.pickle', 'r') as f:
        [right_neural_net, right_fuzzy_sets, right_fuzzy_sets_range] = pickle.load(f)
        f.close()
    print("file loaded")

def identify_pose():
    global arm_pos_cartesian
    arm_pos_cartesian =[]
    global is_identify
    global right_neural_net, right_fuzzy_sets, right_fuzzy_sets_range
    global left_neural_net, left_fuzzy_sets, left_fuzzy_sets_range
    is_identify = True
    while len(arm_pos_cartesian) < 5:
        is_identify = True
    is_identify = False

    # taking average of all the poses...
    scanned = np.array(arm_pos_cartesian)
    pose_left = [scanned[:, 0, 0].mean(),scanned[:, 0, 1].mean(),scanned[:, 1, 0].mean(),scanned[:, 1, 1].mean()]
    pose_right= [scanned[:, 2, 0].mean(),scanned[:, 2, 1].mean(),scanned[:, 3, 0].mean(),scanned[:, 3, 1].mean()]

    left_rule_data = []
    for k, dim in enumerate(pose_left):
        fuzzy_rules = left_fuzzy_sets[k]
        for rule in fuzzy_rules:
            if(dim > min(left_fuzzy_sets_range[k]) and dim < max(left_fuzzy_sets_range[k])):
                temp = fuzz.interp_membership(left_fuzzy_sets_range[k], rule, dim)
            else:
                temp = 0
            left_rule_data.append(temp)
    left_detected_pose = np.argmax(left_neural_net.activate(left_rule_data))

    right_rule_data = []
    for k, dim in enumerate(pose_right):
        fuzzy_rules = right_fuzzy_sets[k]
        for rule in fuzzy_rules:
            if (dim > min(right_fuzzy_sets_range[k]) and dim < max(right_fuzzy_sets_range[k])):
                temp = fuzz.interp_membership(right_fuzzy_sets_range[k], rule, dim)
            else:
                temp = 0
            right_rule_data.append(temp)
    right_detected_pose = np.argmax(right_neural_net.activate(right_rule_data))

    return [right_detected_pose,left_detected_pose]

def get_arm_locations(_skeleton):
    global arm_pos_cartesian
    global is_identify
    is_identify = False
    arm_angles = []
    shoulder_left = np.array([_skeleton[PyKinectV2.JointType_ShoulderLeft].x, _skeleton[PyKinectV2.JointType_ShoulderLeft].y, _skeleton[PyKinectV2.JointType_ShoulderLeft].z])
    shoulder_right = np.array([_skeleton[PyKinectV2.JointType_ShoulderRight].x, _skeleton[PyKinectV2.JointType_ShoulderRight].y, _skeleton[PyKinectV2.JointType_ShoulderRight].z])
    elbow_left = np.array([_skeleton[PyKinectV2.JointType_ElbowLeft].x, _skeleton[PyKinectV2.JointType_ElbowLeft].y, _skeleton[PyKinectV2.JointType_ElbowLeft].z])
    elbow_right = np.array([_skeleton[PyKinectV2.JointType_ElbowRight].x, _skeleton[PyKinectV2.JointType_ElbowRight].y, _skeleton[PyKinectV2.JointType_ElbowRight].z])
    wrist_left = np.array([_skeleton[PyKinectV2.JointType_WristLeft].x, _skeleton[PyKinectV2.JointType_WristLeft].y, _skeleton[PyKinectV2.JointType_WristLeft].z])
    wrist_right = np.array([_skeleton[PyKinectV2.JointType_WristRight].x, _skeleton[PyKinectV2.JointType_WristRight].y, _skeleton[PyKinectV2.JointType_WristRight].z])

    arm_angles.append(translate_to_spherical(wrist_left, elbow_left, shoulder_left))
    arm_angles.append(translate_to_spherical(elbow_left, shoulder_left, shoulder_right))

    arm_angles.append(translate_to_spherical(wrist_right, elbow_right, shoulder_right))
    arm_angles.append(translate_to_spherical(elbow_right, shoulder_right, shoulder_left))

    arm_pos_cartesian.append(arm_angles)

def translate_to_spherical(begin, center, end):
    # get single angle.....
    angle = np.rint(compute_joint_angle(np.subtract(center, begin), np.subtract(center, end)))

    # computing angle direction
    center_xy = (center[0], center[1])
    start_xy = (begin[0], begin[1])
    end_xy = (end[0], end[1])

    direction = angle_cross_2d(np.subtract(center_xy, start_xy), np.subtract(center_xy, end_xy))
    if direction < 0:
        angle = - angle

        # Normal vectors are accurate only when the angle are close to 90 degree
    v1_u = unit_vector(np.subtract(center, begin))
    v2_u = unit_vector(np.subtract(center, end))

    normal = [i * 1000 for i in (np.cross(v1_u, v2_u).tolist())]
    normal_abs = np.absolute(normal).tolist()
    index = normal_abs.index(max(normal_abs))
    if (normal[index] >= 0):
        normal_idx = index*10
    else:
        normal_idx = -index*10

    if (np.absolute(angle) >= 150.0):
        return [np.absolute(angle), 30.0]
    else:
        return [np.absolute(angle), normal_idx]

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def compute_joint_angle(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.rad2deg(np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0)))

def angle_cross_2d(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.cross(v1_u, v2_u)

#############################################################################################
#                               NFS Identification -- ENDS
#############################################################################################



def track_pose(left_pose, right_pose, exercise_id, verbose = True):
    timeout = time.time() + time_for_step  # 12 second of waiting time....
    pose_achieved = True
    half_time = time.time() + time_for_step / 3.0
    encourage = False
    global count ,is_Tracking
    users.create_user_subfolder(exercise_id,count,left_pose,right_pose)
    Pose = identify_pose()
    while (left_pose != left_pose_ID[Pose[1]] or right_pose != right_pose_ID[Pose[0]] ):
        is_Tracking = True

        Pose = identify_pose()

        if time.time() > half_time and not encourage:
            if verbose:
                speech.speak(dialog.encouraging_feedback[random.randint(0, (len(dialog.encouraging_feedback) - 1))])
            encourage = True
        if time.time() > timeout:
            pose_achieved = False
            break

    is_Tracking = False
    if pose_achieved:
        if verbose:
            speech.speak(dialog.positive_feedback[random.randint(0, (len(dialog.positive_feedback) - 1))])
    users.add_status(time_for_step - timeout + time.time(), exercise_id, left_pose, right_pose, pose_achieved)
    count += 1
    return pose_achieved


#  POSE DICTIONARY
pose = {'Left_Up': 'left_up',
        'Left_Down': 'left_down',
        'Left_Front': 'left_front',
        'Left_Side': 'left_side',
        'Left_BendUp': 'left_bend_up',
        'Left_BendFront': 'left_bend_front',
        'Right_Up': 'right_up',
        'Right_Down': 'right_down',
        'Right_Front': 'right_front',
        'Right_Side': 'right_side',
        'Right_BendUp': 'right_bend_up',
        'Right_BendFront': 'right_bend_front', }


left_pose_ID = {0:"left_side",
                1:"left_up",
                2:"left_front",
                3:"left_down",
                4:"left_bend_up",
                5:"left_bend_front",
          }

right_pose_ID = {   0:"right_side",
                    1:"right_up",
                    2:"right_front",
                    3:"right_down",
                    4:"right_bend_up",
                    5:"right_bend_front",
          }


