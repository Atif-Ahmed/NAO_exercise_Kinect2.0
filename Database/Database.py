import json
import sqlite3


def setup_db():
    connection = sqlite3.connect("Database/NAO_PROJECT.db")
    connection.execute("CREATE TABLE IF NOT EXISTS Users ( "
                       "id INTEGER PRIMARY KEY, "
                       "name TEXT NOT NULL, "
                       "password TEXT NOT NULL, "
                       "age TEXT NOT NULL, "
                       "gender TEXT NOT NULL,"
                       "session INTEGER NOT NULL)")

    # Stats table
    connection.execute("CREATE TABLE IF NOT EXISTS History ( "
                       "id INTEGER PRIMARY KEY,"
                       "user_id INTEGER NOT NULL, "
                       "session INTEGER NOT NULL, "
                       "exercise_id INTEGER NOT NULL,"
                       "is_successful INTEGER NOT NULL, "
                       "score REAL NOT NULL, "
                       "response_time REAL NOT NULL,"
                       "left_pose TEXT NOT NULL,"
                       "right_pose TEXT NOT NULL,"
                       "arm TEXT NOT NULL)")
    connection.close()


def verify_login(username, password):
    db_conn = sqlite3.connect("Database/NAO_PROJECT.db")
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE name = ? AND password = ?", (str(username), str(password)))
    data = cursor.fetchall()
    if not data:
        print("Failed")
        cursor.close()
        db_conn.close()
        return []
    else:
        print("Success")
        cursor.close()
        db_conn.close()
        return data


def add_user(username, password, age, gender):
    db_conn = sqlite3.connect("Database/NAO_PROJECT.db")
    db_conn.execute("""INSERT INTO Users ( name, password, age, gender, session)
    VALUES(?,?,?,?,?)""", (str(username), str(password), str(age), str(gender), int(0)))
    db_conn.commit()
    db_conn.close()


def add_history(user_id, session, stats):
    db_conn = sqlite3.connect("Database/NAO_PROJECT.db")
    for stat in stats:
        arm_data = arm_to_dict(stat.arm)
        arm_data = json.dumps(arm_data)
        db_conn.execute("""INSERT INTO History ( user_id, session, exercise_id, is_successful, score, response_time, left_pose, right_pose, arm) VALUES(?,?,?,?,?,?,?,?,?)""",
                        (int(user_id), int(session), int(stat.exercise_id), stat.is_successful, stat.score, stat.response_time,str(stat.exercise_pose.left),
                         str(stat.exercise_pose.right), (arm_data)))
    db_conn.commit()
    db_conn.execute("""UPDATE Users SET session = ? WHERE id=?""", (session, user_id))
    db_conn.commit()
    db_conn.close()


def arm_to_dict(arm):
    arm_dict = {"left": {"position": {"shoulder": arm.left.position.shoulder,
                                  "elbow": arm.left.position.elbow,
                                  "wrist": arm.left.position.wrist},
                     "angles": {"shoulder": {"angle": arm.left.angles.shoulder.angle,
                                             "orientation": arm.left.angles.shoulder.orientation},
                                "elbow": {"angle": arm.left.angles.elbow.angle,
                                          "orientation": arm.left.angles.elbow.orientation}}},

            "right": {"position": {"shoulder": arm.right.position.shoulder,
                                   "elbow": arm.right.position.elbow,
                                   "wrist": arm.right.position.wrist},
                      "angles": {"shoulder": {"angle": arm.left.angles.shoulder.angle,
                                              "orientation": arm.left.angles.shoulder.orientation},
                                 "elbow": {"angle": arm.left.angles.elbow.angle,
                                           "orientation": arm.left.angles.elbow.orientation}}
                      }}
    return arm_dict
