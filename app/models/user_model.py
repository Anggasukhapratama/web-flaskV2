# app/models/user_model.py
from app import mysql

class UserModel:
    @staticmethod
    def get_user_by_username(username):
        """Mengambil user berdasarkan username."""
        cursor = mysql.connection.cursor()
        query = "SELECT id, username, password FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        cursor.close()
        return user
