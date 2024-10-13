# models.py

from config import get_db_connection


def get_all_users():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    db.close()
    return users


def get_all_personal():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT personal FROM users")
    users_personal = cursor.fetchall()
    cursor.close()
    db.close()
    return users_personal


def get_user_by_credentials(username, password):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username = %s AND password = %s",
        (username, password),
    )
    user = cursor.fetchone()
    cursor.close()
    db.close()
    return user


def insert_user(username, password, age, email, personal_info):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO users (username, password, age, email, personal) VALUES (%s, %s, %s, %s, %s)",
        (username, password, age, email, personal_info),
    )
    db.commit()
    rowcount = cursor.rowcount
    cursor.close()
    db.close()
    return rowcount > 0
