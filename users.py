import os
import time
import kinect_interface as kinect
import pygame
from PyQt4 import QtGui
from PyQt4 import QtCore
import Exercise.exercise_result as ex_result
import arm_tracking as arm
import Database.Database as Db

user_table = {"user_id": 0,
              "name": 1,
              "password": 2,
              "age": 3,
              "gender": 4,
              "session": 5}
signup = None
login = None
userData = None

stats = []

user_data_path = "Database/userData/"
current_user_subFolder_path = ""


class UserSignup(object):
    def setup_ui(self, sign_up):
        sign_up.setObjectName("signup")
        sign_up.resize(246, 212)
        sign_up.setStyleSheet("QDialog{    \n"
                              "background-color: qlineargradient(spread:pad, x1:0.477273, y1:1, x2:0.489, y2:0, "
                              "stop:0 rgba(0, 210, 191, 255), "
                              "stop:1 rgba(152, 214, 225, 255));\n "
                              "}\n"
                              "QPushButton{    \n"
                              "background-color: qlineargradient(spread:reflect, x1:0.471, y1:0.00568182, x2:0.466, "
                              "y2:0.863682, stop:0.125 rgba(255, 255, 255, 255), stop:0.886364 rgba(255, 219, 18, "
                              "255));\n "
                              "border:none;\n"
                              "}")
        self.pushButton_signup = QtGui.QPushButton(sign_up)
        self.pushButton_signup.setGeometry(QtCore.QRect(130, 160, 75, 23))
        self.pushButton_signup.setObjectName("pushButton_signup")
        self.label_username = QtGui.QLabel(sign_up)
        self.label_username.setGeometry(QtCore.QRect(20, 30, 61, 16))
        self.label_username.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_username.setObjectName("label_username")
        self.label_password = QtGui.QLabel(sign_up)
        self.label_password.setGeometry(QtCore.QRect(20, 60, 61, 16))
        self.label_password.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_password.setObjectName("label_password")
        self.label_age = QtGui.QLabel(sign_up)
        self.label_age.setGeometry(QtCore.QRect(20, 90, 61, 16))
        self.label_age.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_age.setObjectName("label_age")
        self.label_gender = QtGui.QLabel(sign_up)
        self.label_gender.setGeometry(QtCore.QRect(20, 120, 61, 16))
        self.label_gender.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_gender.setObjectName("label_gender")
        self.lineEdit_username = QtGui.QLineEdit(sign_up)
        self.lineEdit_username.setGeometry(QtCore.QRect(90, 30, 113, 20))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_password = QtGui.QLineEdit(sign_up)
        self.lineEdit_password.setGeometry(QtCore.QRect(90, 60, 113, 20))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_age = QtGui.QLineEdit(sign_up)
        self.lineEdit_age.setGeometry(QtCore.QRect(90, 90, 113, 20))
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.radioButton_male = QtGui.QRadioButton(sign_up)
        self.radioButton_male.setGeometry(QtCore.QRect(90, 120, 51, 17))
        self.radioButton_male.setObjectName("radioButton_male")
        self.radioButton_female = QtGui.QRadioButton(sign_up)
        self.radioButton_female.setGeometry(QtCore.QRect(150, 120, 61, 17))
        self.radioButton_female.setObjectName("radioButton_female")

        #####################################################################################
        self.pushButton_signup.clicked.connect(self.add_user)

        self.retranslate_ui(sign_up)
        QtCore.QMetaObject.connectSlotsByName(sign_up)
        sign_up.setTabOrder(self.lineEdit_username, self.lineEdit_password)
        sign_up.setTabOrder(self.lineEdit_password, self.lineEdit_age)
        sign_up.setTabOrder(self.lineEdit_age, self.radioButton_male)
        sign_up.setTabOrder(self.radioButton_male, self.radioButton_female)
        sign_up.setTabOrder(self.radioButton_female, self.pushButton_signup)

    def retranslate_ui(self, _signup):
        _signup.setWindowTitle("SignUp Screen")
        self.pushButton_signup.setText("SignUp")
        self.label_username.setText("UserName")
        self.label_password.setText("Password")
        self.label_age.setText("Age")
        self.label_gender.setText("Gender")
        self.radioButton_male.setText("Male")
        self.radioButton_female.setText("Female")

    def add_user(self):
        name = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        age = self.lineEdit_age.text()
        if self.radioButton_male.isChecked():
            gender = 'Male'
        else:
            gender = 'Female'

        if name == '' or password == '' or age == '' or gender == '':
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Critical)
            msg.setText("Invalid or incomplete information provided for new user")
            msg.setWindowTitle("Error Message")
            msg.exec_()
        else:
            Db.add_user(name, password, age, gender)
            signup.close()


class UserLogin(object):
    def setup_ui(self, _login):
        _login.setObjectName("Login")
        _login.resize(255, 150)
        _login.setStyleSheet("QDialog{\n"
                             "    \n"
                             "background-color: qlineargradient(spread:pad, x1:0.477273, y1:1, x2:0.489, y2:0, "
                             "stop:0 rgba(0, 210, 191, 255), "
                             "stop:1 rgba(152, 214, 225, 255));\n "
                             "}\n"
                             "QPushButton#pushButton_login{    \n"
                             "background-color: qlineargradient(spread:reflect, x1:0.471, y1:0.00568182, x2:0.466, "
                             "y2:0.863682, stop:0.125 rgba(255, 255, 255, 255), stop:0.886364 rgba(255, 219, 18, "
                             "255));\n "
                             "    border:none;\n"
                             "}")
        self.label_username = QtGui.QLabel(_login)
        self.label_username.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label_username.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_username.setObjectName("label_username")
        self.label_password = QtGui.QLabel(_login)
        self.label_password.setGeometry(QtCore.QRect(20, 50, 51, 16))
        self.label_password.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_password.setObjectName("label_password")
        self.lineEdit_username = QtGui.QLineEdit(_login)
        self.lineEdit_username.setGeometry(QtCore.QRect(80, 20, 141, 20))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_password = QtGui.QLineEdit(_login)
        self.lineEdit_password.setGeometry(QtCore.QRect(80, 50, 141, 20))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.pushButton_login = QtGui.QPushButton(_login)
        self.pushButton_login.setGeometry(QtCore.QRect(160, 80, 61, 21))
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_signup = QtGui.QPushButton(_login)
        self.pushButton_signup.setGeometry(QtCore.QRect(20, 120, 201, 20))
        font = QtGui.QFont()
        font.setItalic(True)
        font.setUnderline(True)
        self.pushButton_signup.setFont(font)
        self.pushButton_signup.setAutoFillBackground(False)
        self.pushButton_signup.setStyleSheet("")
        self.pushButton_signup.setAutoDefault(True)
        self.pushButton_signup.setFlat(True)
        self.pushButton_signup.setObjectName("pushButton_signup")

        ###############################################################################
        self.pushButton_login.clicked.connect(self.login_check)
        self.pushButton_signup.clicked.connect(self.open_signup_screen)

        self.retranslate_ui(_login)
        QtCore.QMetaObject.connectSlotsByName(_login)

    def retranslate_ui(self, _login):
        _login.setWindowTitle("Login Screen")
        self.label_username.setText("User Name")
        self.label_password.setText("Password")
        self.pushButton_login.setText("Login")
        self.pushButton_signup.setText("Create New User Account")



    def login_check(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        # check the database for entry
        global userData
        userData = Db.verify_login(username, password)
        if not userData:
            pass
        else:
            userData = list(userData[0])
            userData[user_table["session"]] += 1
            QtCore.QCoreApplication.instance().quit()

    @staticmethod
    def open_signup_screen():
        global signup
        signup = QtGui.QDialog()
        signup.ui = UserSignup()
        signup.ui.setup_ui(signup)
        signup.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        signup.exec_()






def login_screen():
    # setup the database if it does not exists....
    if not os.path.isfile("Database/NAO_PROJECT.db"):
        print("Creating new Database...")
        Db.setup_db()

    import sys
    global login
    app = QtGui.QApplication(sys.argv)
    login = QtGui.QDialog()
    ui = UserLogin()
    ui.setup_ui(login)
    login.show()

    app.exec_()


def get_user_id():
    return userData[user_table["user_id"]]


def get_user_name():
    return userData[user_table["name"]]


def get_user_age():
    return userData[user_table["age"]]


def get_user_gender():
    return userData[user_table["gender"]]


def get_session_id():
    return userData[user_table["session"]]


def add_status(response_time, exercise_id, pose_id_left, pose_id_right, is_successful):
    global stats
    pose_id_right = str(pose_id_right).replace("is_", "")
    pose_id_left = str(pose_id_left).replace("is_", "")
    stats.append(ex_result.save_status(response_time, exercise_id, pose_id_left, pose_id_right, is_successful))


def get_total_score():
    global stats
    total_score = 0
    for stat in stats:
        total_score = total_score + stat.score
    return total_score


def save_stat_db():
    Db.add_history(get_user_id(), get_session_id(), stats)


def create_user_folder():
    global user_data_path
    user_data_path = user_data_path + get_user_name() + "/session" + str(get_session_id())
    if not os.path.exists(user_data_path):
        os.makedirs(user_data_path)


def create_user_subfolder(ex_id,num,left,right):
    global user_data_path
    global current_user_subFolder_path
    current_user_subFolder_path = (user_data_path + "/Exercise" + str(ex_id) +
                                   "/Step=" + str(num) +
                                   " Left=" + str(left).replace("left_","")+
                                   " Right=" + str(right).replace("right_",""))
    if not os.path.exists(current_user_subFolder_path):
        os.makedirs(current_user_subFolder_path)

    f = open(current_user_subFolder_path + "/data.csv","w+")
    f.write("LeftShoulder,"
            "RightShoulder,"
            "LeftElbow,"
            "RightElbow,"
            "LeftWrist,"
            "RightWrist,"
            "LeftShoulderAngle,"
            "LeftShoulderNormal,"
            "RightShoulderAngle,"
            "RightShoulderNormal,"
            "LeftElbowAngle,"
            "LeftElbowNormal,"
            "RightElbowAngle,"
            "RightElbowNormal\n" )
    f.close()

def record_user_state():
    #record Image of user
    pygame.image.save(kinect.screen_cpy, current_user_subFolder_path + "/capture_" +str(time.time())+ ".jpg")

    #record user stats as csv
    f = open(current_user_subFolder_path+"/data.csv","a+")
    f.write("%s|%s|%s"%arm.pos_shoulder_left +","+
            "%s|%s|%s"%arm.pos_shoulder_right +","+
            "%s|%s|%s"%arm.pos_elbow_left +","+
            "%s|%s|%s"%arm.pos_elbow_right +","+
            "%s|%s|%s"%arm.pos_wrist_left +","+
            "%s|%s|%s"%arm.pos_wrist_right +","+
            str(arm.shoulder_left_angle) +","+
            str(arm.shoulder_left_normal) +","+
            str(arm.shoulder_right_angle)+","+
            str(arm.shoulder_right_normal) +","+
            str(arm.elbow_left_angle) +","+
            str(arm.elbow_left_normal) +","+
            str(arm.elbow_right_angle) +","+
            str(arm.elbow_left_normal) +"\n")
    f.close()
    return 0
