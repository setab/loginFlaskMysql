# config.py
import mysql.connector


class Config:
    SECRET_KEY = "I lOve me".encode("utf8")
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"  # Your MySQL username
    MYSQL_PASSWORD = "100123"  # Your MySQL password
    MYSQL_DATABASE = "login_db2"
    MYSQL_PORT = 33061


def get_db_connection():
    return mysql.connector.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DATABASE,
        port=Config.MYSQL_PORT,
    )
