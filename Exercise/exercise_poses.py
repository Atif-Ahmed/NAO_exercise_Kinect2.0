import nao_interface as nao_robot

movementSpeed = 0.90000


def left_front():
    names = list()
    times = list()
    keys = list()

    names.append("LElbowRoll")
    times.append([movementSpeed])
    keys.append([-0.00873])

    names.append("LElbowYaw")
    times.append([movementSpeed])
    keys.append([-0.00001])

    names.append("LHand")
    times.append([movementSpeed])
    keys.append([0.00000])

    names.append("LShoulderPitch")
    times.append([movementSpeed])
    keys.append([-0.00000])

    names.append("LShoulderRoll")
    times.append([movementSpeed])
    keys.append([0.01810])

    names.append("LWristYaw")
    times.append([movementSpeed])
    keys.append([0.00000])

    try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        # motion = ALProxy("ALMotion", IP, 9559)

        nao_robot.motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print err


def right_front():
    names = list()
    times = list()
    keys = list()

    names.append("RElbowRoll")
    times.append([movementSpeed])
    keys.append([0.00877])

    names.append("RElbowYaw")
    times.append([movementSpeed])
    keys.append([0.00001])

    names.append("RHand")
    times.append([movementSpeed])
    keys.append([0.00000])

    names.append("RShoulderPitch")
    times.append([movementSpeed])
    keys.append([0.00000])

    names.append("RShoulderRoll")
    times.append([movementSpeed])
    keys.append([-0.01810])

    names.append("RWristYaw")
    times.append([movementSpeed])
    keys.append([0.00000])

    try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        # motion = ALProxy("ALMotion", IP, 9559)

        nao_robot.motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print err


def left_side():
    names = list()
    times = list()
    keys = list()

    names.append("LElbowRoll")
    times.append([movementSpeed])
    keys.append([-0.00873])

    names.append("LElbowYaw")
    times.append([movementSpeed])
    keys.append([0.00270])

    names.append("LHand")
    times.append([movementSpeed])
    keys.append([0.00000])

    names.append("LShoulderPitch")
    times.append([movementSpeed])
    keys.append([0.00000])

    names.append("LShoulderRoll")
    times.append([movementSpeed])
    keys.append([1.57080])

    names.append("LWristYaw")
    times.append([movementSpeed])
    keys.append([0.00000])

    try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        # motion = ALProxy("ALMotion", IP, 9559)

        nao_robot.motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print err


def right_side():
    names = list()
    times = list()
    keys = list()

    names.append("RElbowRoll")
    times.append([movementSpeed])
    keys.append([0.01571])

    names.append("RElbowYaw")
    times.append([movementSpeed])
    keys.append([-0.00270])

    names.append("RHand")
    times.append([movementSpeed])
    keys.append([0.00000])

    names.append("RShoulderPitch")
    times.append([movementSpeed])
    keys.append([0.00000])

    names.append("RShoulderRoll")
    times.append([movementSpeed])
    keys.append([-1.57080])

    names.append("RWristYaw")
    times.append([movementSpeed])
    keys.append([-0.00000])

    try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        # motion = ALProxy("ALMotion", IP, 9559)

        nao_robot.motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print err


def left_up():
    names = list()
    times = list()
    keys = list()

    names.append("LElbowRoll")
    times.append([movementSpeed])
    keys.append([-0.00873])

    names.append("LElbowYaw")
    times.append([movementSpeed])
    keys.append([0.00015])

    names.append("LHand")
    times.append([movementSpeed])
    keys.append([0.00000])

    names.append("LShoulderPitch")
    times.append([movementSpeed])
    keys.append([-1.22173])

    names.append("LShoulderRoll")
    times.append([movementSpeed])
    keys.append([0.43633])

    names.append("LWristYaw")
    times.append([movementSpeed])
    keys.append([-0.00000])

    try:
        nao_robot.motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print err


def right_up():
    names = list()
    times = list()
    keys = list()

    names.append("RElbowRoll")
    times.append([movementSpeed])
    keys.append([0.00917])

    names.append("RElbowYaw")
    times.append([movementSpeed])
    keys.append([-0.00015])

    names.append("RHand")
    times.append([movementSpeed])
    keys.append([0.00000])

    names.append("RShoulderPitch")
    times.append([movementSpeed])
    keys.append([-1.22173])

    names.append("RShoulderRoll")
    times.append([movementSpeed])
    keys.append([-0.43633])

    names.append("RWristYaw")
    times.append([movementSpeed])
    keys.append([0.00000])

    try:
        nao_robot.motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print err


def left_down():
    names = list()
    times = list()
    keys = list()

    names.append("LElbowRoll")
    times.append([movementSpeed])
    keys.append([-0.00873])

    names.append("LElbowYaw")
    times.append([movementSpeed])
    keys.append([0.00038])

    names.append("LHand")
    times.append([movementSpeed])
    keys.append([0.00000])

    names.append("LShoulderPitch")
    times.append([movementSpeed])
    keys.append([1.55111])

    names.append("LShoulderRoll")
    times.append([movementSpeed])
    keys.append([0.18413])

    names.append("LWristYaw")
    times.append([movementSpeed])
    keys.append([0.00000])

    try:
        nao_robot.motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print err


def right_down():
    names = list()
    times = list()
    keys = list()

    names.append("RElbowRoll")
    times.append([movementSpeed])
    keys.append([0.00873])

    names.append("RElbowYaw")
    times.append([movementSpeed])
    keys.append([-0.00038])

    names.append("RHand")
    times.append([movementSpeed])
    keys.append([0.00000])

    names.append("RShoulderPitch")
    times.append([movementSpeed])
    keys.append([1.55111])

    names.append("RShoulderRoll")
    times.append([movementSpeed])
    keys.append([-0.18413])

    names.append("RWristYaw")
    times.append([movementSpeed])
    keys.append([0.00000])

    try:
        nao_robot.motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print err


def left_bend_front():
    names = list()
    times = list()
    keys = list()

    names.append("LElbowRoll")
    times.append([movementSpeed])
    keys.append([-1.55334])

    names.append("LElbowYaw")
    times.append([movementSpeed])
    keys.append([0.00270])

    names.append("LHand")
    times.append([movementSpeed])
    keys.append([0.00000])

    names.append("LShoulderPitch")
    times.append([movementSpeed])
    keys.append([-0.00000])

    names.append("LShoulderRoll")
    times.append([movementSpeed])
    keys.append([1.57080])

    names.append("LWristYaw")
    times.append([movementSpeed])
    keys.append([-0.00000])

    try:
        nao_robot.motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print err


def right_bend_front():
    names = list()
    times = list()
    keys = list()

    names.append("RElbowRoll")
    times.append([movementSpeed])
    keys.append([1.55334])

    names.append("RElbowYaw")
    times.append([movementSpeed])
    keys.append([-0.00270])

    names.append("RHand")
    times.append([movementSpeed])
    keys.append([0.00000])

    names.append("RShoulderPitch")
    times.append([movementSpeed])
    keys.append([0.00000])

    names.append("RShoulderRoll")
    times.append([movementSpeed])
    keys.append([-1.57080])

    names.append("RWristYaw")
    times.append([movementSpeed])
    keys.append([0.00000])

    try:
        nao_robot.motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print err
        
        
def left_bend_up():
    names = list()
    times = list()
    keys = list()

    names.append("LElbowRoll")
    times.append([movementSpeed])
    keys.append([-1.55334])

    names.append("LElbowYaw")
    times.append([movementSpeed])
    keys.append([0.00270])

    names.append("LHand")
    times.append([movementSpeed])
    keys.append([0.00000])

    names.append("LShoulderPitch")
    times.append([movementSpeed])
    keys.append([-1.57080])

    names.append("LShoulderRoll")
    times.append([movementSpeed])
    keys.append([1.57080])

    names.append("LWristYaw")
    times.append([movementSpeed])
    keys.append([-0.00000])

    try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        # motion = ALProxy("ALMotion", IP, 9559)
        nao_robot.motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print err


def right_bend_up():
    names = list()
    times = list()
    keys = list()

    names.append("RElbowRoll")
    times.append([movementSpeed])
    keys.append([1.55334])

    names.append("RElbowYaw")
    times.append([movementSpeed])
    keys.append([-0.00270])

    names.append("RHand")
    times.append([movementSpeed])
    keys.append([0.00000])

    names.append("RShoulderPitch")
    times.append([movementSpeed])
    keys.append([-1.57080])

    names.append("RShoulderRoll")
    times.append([movementSpeed])
    keys.append([-1.64934])

    names.append("RWristYaw")
    times.append([movementSpeed])
    keys.append([0.00000])

    try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        # motion = ALProxy("ALMotion", IP, 9559)
        nao_robot.motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print err
