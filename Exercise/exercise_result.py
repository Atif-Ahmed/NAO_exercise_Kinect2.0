import arm_tracking as user_arm_tracking
import exercise_tracking as ex_track
# User Data
#       |---- is Successful
#       |---- response time
#       |---- exercise ID
#       |---- score
#       |---- exercise pose
#       |           |-------- left arm pose
#       |           |-------- right arm pose
#       |---- arm
#               |------ left
#                           |---- position
#                           |           |------ Shoulder
#                           |           |------- Elbow
#                           |           |------ Wrist
#                           |---- angle
#                                   |----- Elbow
#                                   |       |---- Angle
#                                   |       |----- Orientation
#                                   |----- Shoulder
#                                           |---- Angle
#                                           |----- Orientation

class Angle:
    def __init__(self, angle, orientation):
        self.angle = angle
        self.orientation = orientation


class ArmAngles:
    def __init__(self, elbow_angle, elbow_orientation, should_angle, shoulder_orientation):
        self.elbow = Angle(elbow_angle, elbow_orientation)
        self.shoulder = Angle(should_angle, shoulder_orientation)


class Position:
    def __init__(self, shoulder, elbow, wrist):
        self.shoulder = shoulder
        self.elbow = elbow
        self.wrist = wrist


class ArmStat:
    def __init__(self, shoulder, elbow, wrist, elbow_angle, elbow_orientation, shoulder_angle, shoulder_orientation):
        self.position = Position(shoulder, elbow, wrist)
        self.angles = ArmAngles(elbow_angle, elbow_orientation, shoulder_angle, shoulder_orientation)


class Arm:
    def __init__(self):
        self.left = ArmStat(user_arm_tracking.pos_shoulder_left, user_arm_tracking.pos_elbow_left, user_arm_tracking.pos_wrist_left,
                            user_arm_tracking.elbow_left_angle, user_arm_tracking.elbow_left_normal,
                            user_arm_tracking.shoulder_left_angle, user_arm_tracking.shoulder_left_normal)
        self.right = ArmStat(user_arm_tracking.pos_shoulder_right, user_arm_tracking.pos_elbow_right, user_arm_tracking.pos_wrist_right,
                             user_arm_tracking.elbow_right_angle, user_arm_tracking.elbow_right_normal,
                             user_arm_tracking.shoulder_left_angle, user_arm_tracking.shoulder_left_normal)


class ExercisePose:
    def __init__(self, pose_left, pose_right):
        self.left = pose_left
        self.right = pose_right


class UserStatus:
    def __init__(self, response_time, exercise_id, pose_id_left, pose_id_right, is_successful):
        self.is_successful = is_successful
        self.arm = Arm()
        self.response_time = response_time
        self.exercise_id = exercise_id
        self.exercise_pose = ExercisePose(pose_id_left, pose_id_right)
        self.score = 0
        self.compute_score()

    def compute_score(self):
        # TODO - make improvement in scoring.... system.
        self.score = (ex_track.time_for_step - self.response_time) / ex_track.time_for_step * 100
        pass


def save_status(response_time, exercise_id, pose_id_left, pose_id_right, is_successful):
    new_status = UserStatus(response_time, exercise_id, pose_id_left, pose_id_right, is_successful)
    return new_status


