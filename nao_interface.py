from naoqi import ALProxy
import Exercise.exercise_1 as ex1
import Exercise.exercise_2 as ex2
import Exercise.exercise_3 as ex3

tts = None
posture = None
motion = None

NAO_sim_ip = "127.0.0.1"  # for Lab Environment
#NAO_sim_ip = "192.168.0.103"  # for Laptop
# NAO_sim_ip = "10.24.110.160"  # for Lab PC
NAO_robot_ip = "192.168.0.100"
NAO_port_id = 9559


def init(is_simulate):
    global tts
    global posture
    global motion
    if is_simulate:
        tts = ALProxy("ALTextToSpeech", NAO_sim_ip, NAO_port_id)
        posture = ALProxy("ALRobotPosture", NAO_sim_ip, NAO_port_id)
        motion = ALProxy("ALMotion", NAO_sim_ip, NAO_port_id)
    else:
        tts = ALProxy("ALTextToSpeech", NAO_robot_ip, NAO_port_id)
        posture = ALProxy("ALRobotPosture", NAO_robot_ip, NAO_port_id)
        motion = ALProxy("ALMotion", NAO_sim_ip, NAO_port_id)


def start_session():
    # Start Exercise 1......
    ex1.start(posture)
    ex2.start(posture)
    ex3.start(posture)


def get_tts():
    # type: () -> object
    return tts
