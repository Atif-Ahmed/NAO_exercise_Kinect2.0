from collections import deque

import matplotlib.pyplot as plt
import numpy as npy
from pykinect2 import PyKinectV2

# the four required angles
elbow_left_angle = None
elbow_right_angle = None
shoulder_left_angle = None
shoulder_right_angle = None
elbow_left_normal = None
elbow_right_normal = None
shoulder_left_normal = None
shoulder_right_normal = None

pos_shoulder_left = None
pos_shoulder_right = None
pos_elbow_left = None
pos_elbow_right = None
pos_wrist_left = None
pos_wrist_right = None

num_tracked_lengths = 500

length_arm_left = [deque(0 for x1 in xrange(num_tracked_lengths)),  # upper arm
                   deque(0 for x2 in xrange(num_tracked_lengths)),  # lower arm
                   deque(0 for x3 in xrange(num_tracked_lengths))]  # hand

length_arm_right = [deque(0 for x4 in xrange(num_tracked_lengths)),  # upper arm
                    deque(0 for x5 in xrange(num_tracked_lengths)),  # lower arm
                    deque(0 for x6 in xrange(num_tracked_lengths))]  # hand


# keep track of last N entries arm lengths and angles
def update(skeleton):
    # pop out older values

    for i in range(len(length_arm_left)):
        length_arm_left[i].popleft()
        length_arm_right[i].popleft()

    # append the new values
    length_arm_left[0].append(compute_length(skeleton, PyKinectV2.JointType_ShoulderLeft, PyKinectV2.JointType_ElbowLeft))
    length_arm_left[1].append(compute_length(skeleton, PyKinectV2.JointType_ElbowLeft, PyKinectV2.JointType_WristLeft))
    length_arm_left[2].append(compute_length(skeleton, PyKinectV2.JointType_WristLeft, PyKinectV2.JointType_HandLeft))

    length_arm_right[0].append(compute_length(skeleton, PyKinectV2.JointType_ShoulderRight, PyKinectV2.JointType_ElbowRight))
    length_arm_right[1].append(compute_length(skeleton, PyKinectV2.JointType_ElbowRight, PyKinectV2.JointType_WristRight))
    length_arm_right[2].append(compute_length(skeleton, PyKinectV2.JointType_WristRight, PyKinectV2.JointType_HandRight))


# convert the vector data to array data for processing
def vec2array(vector):
    result = npy.array([vector.x, vector.y, vector.z])
    return result


def display_graph():
    fig, (axis1, axis2) = plt.subplots(nrows=2)
    fig.suptitle('Graph for Arm Lengths')
    axis1.set_title('Left Arm Lengths')
    axis1.plot(length_arm_left[0], 'r-', label='Left Upper Arm', linewidth=2)
    axis1.plot(length_arm_left[1], 'g-', label='Left Lower Arm', linewidth=2)
    axis1.plot(length_arm_left[2], 'b-', label='Left Hand', linewidth=2)

    axis2.set_title('Right Arm Lengths')
    axis2.plot(length_arm_right[0], 'r-', label='Right Upper Arm', linewidth=2)
    axis2.plot(length_arm_right[1], 'g-', label='Right Lower Arm', linewidth=2)
    axis2.plot(length_arm_right[2], 'b-', label='Hand Arm', linewidth=2)
    plt.show()


def compute_length(skeleton, point1, point2):
    return npy.linalg.norm(vec2array(skeleton[point1]) - vec2array(skeleton[point2]))


# Computation of angles of joints from skeleton....##

def compute_angles(_skeleton):
    global elbow_left_angle, elbow_right_angle, shoulder_left_angle, shoulder_right_angle
    global elbow_left_normal, elbow_right_normal, shoulder_left_normal, shoulder_right_normal
    global pos_shoulder_left, pos_shoulder_right, pos_elbow_left, pos_elbow_right, pos_wrist_left, pos_wrist_right

    pos_shoulder_left = (
        _skeleton[PyKinectV2.JointType_ShoulderLeft].x,
        _skeleton[PyKinectV2.JointType_ShoulderLeft].y,
        _skeleton[PyKinectV2.JointType_ShoulderLeft].z)

    pos_shoulder_right = (
        _skeleton[PyKinectV2.JointType_ShoulderRight].x,
        _skeleton[PyKinectV2.JointType_ShoulderRight].y,
        _skeleton[PyKinectV2.JointType_ShoulderRight].z)

    pos_elbow_left = (
        _skeleton[PyKinectV2.JointType_ElbowLeft].x,
        _skeleton[PyKinectV2.JointType_ElbowLeft].y,
        _skeleton[PyKinectV2.JointType_ElbowLeft].z)

    pos_elbow_right = (
        _skeleton[PyKinectV2.JointType_ElbowRight].x,
        _skeleton[PyKinectV2.JointType_ElbowRight].y,
        _skeleton[PyKinectV2.JointType_ElbowRight].z)

    pos_wrist_left = (
        _skeleton[PyKinectV2.JointType_WristLeft].x,
        _skeleton[PyKinectV2.JointType_WristLeft].y,
        _skeleton[PyKinectV2.JointType_WristLeft].z)

    pos_wrist_right = (
        _skeleton[PyKinectV2.JointType_WristRight].x,
        _skeleton[PyKinectV2.JointType_WristRight].y,
        _skeleton[PyKinectV2.JointType_WristRight].z)

    elbow_left_angle = - get_3d_angles(pos_wrist_left, pos_elbow_left, pos_shoulder_left)
    elbow_right_angle = get_3d_angles(pos_wrist_right, pos_elbow_right, pos_shoulder_right)
    shoulder_left_angle = - get_3d_angles(pos_elbow_left, pos_shoulder_left, pos_shoulder_right)
    shoulder_right_angle = get_3d_angles(pos_elbow_right, pos_shoulder_right, pos_shoulder_left)

    elbow_left_normal = get_normal_vector(pos_wrist_left, pos_elbow_left, pos_shoulder_left)
    elbow_right_normal = get_normal_vector(pos_wrist_right, pos_elbow_right, pos_shoulder_right)
    shoulder_left_normal = get_normal_vector(pos_elbow_left, pos_shoulder_left, pos_shoulder_right)
    shoulder_right_normal = get_normal_vector(pos_elbow_right, pos_shoulder_right, pos_shoulder_left)


def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / npy.linalg.norm(vector)


def compute_joint_angle(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return npy.rad2deg(npy.arccos(npy.clip(npy.dot(v1_u, v2_u), -1.0, 1.0)))


def angle_cross_2d(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return npy.cross(v1_u, v2_u)


def get_3d_angles(start, center, end):
    # get single angle.....
    angle = npy.rint(compute_joint_angle(npy.subtract(center, start), npy.subtract(center, end)))

    # computing angle direction
    center_xy = (center[0], center[1])
    start_xy = (start[0], start[1])
    end_xy = (end[0], end[1])

    direction = angle_cross_2d(npy.subtract(center_xy, start_xy), npy.subtract(center_xy, end_xy))
    if direction < 0:
        angle = - angle
    return angle


def get_normal_vector(start, center, end):
    # Normal vectors are accurate only when the angle are close to 90 degree
    v1_u = unit_vector(npy.subtract(center, start))
    v2_u = unit_vector(npy.subtract(center, end))

    normal = [i * 1000 for i in (npy.cross(v1_u, v2_u).tolist())]
    normal = npy.absolute(npy.rint(normal)).tolist()
    return normal.index(max(normal))
