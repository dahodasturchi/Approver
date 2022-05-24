import sqlite3




class Database:
    def __init__(self, db_file_path = "./data/main.db") -> None:
        self.db_file_path = db_file_path

    @property
    def connection(self):
        return sqlite3.connect(self.db_file_path)

    def execute(self, 
            sql: str, 
            parameters: tuple = None, 
            fetchone=False, 
            fetchall=False, 
            commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())
    def create_users_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users(
            user_id int,
            full_name varchar(256),
            lang_code str,
            username varchar(64))"""
        self.execute(sql=sql, commit=True)
    
    def create_chats_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Chats(
            chat_id int,
            chat_title varchar(256),
            chat_type str,
            username varchar(64))"""
        self.execute(sql=sql, commit=True)

    def add_user(
        self, 
        user_id: int, 
        full_name: str, 
        lang_code: str, 
        username: str = None
        ):
        if self.select_user(user_id) != 0:
            return
        sql = """
        INSERT INTO Users (user_id, full_name, lang_code, username) VALUES (?,?,?,?)"""
        self.execute(
            sql=sql, 
            parameters=(user_id, full_name, lang_code, username,), commit=True)
    
    def add_chat(self,
            chat_id: int,
            chat_title: str,
            chat_type: str,
            username: str = None):
        if self.select_chat(chat_id=chat_id) != 0:
            return
        sql = """
        INSERT INTO Chats(chat_id, chat_title, chat_type, username) VALUES(?,?,?,?)"""
        self.execute(sql=sql, parameters=(
            chat_id, chat_title, chat_type, username,
        ), 
        commit=True)

    def select_user(self, user_id):
        sql = """
        SELECT * FROM Users WHERE user_id = ?"""
        res = self.execute(sql=sql, parameters=(user_id,), fetchone=True)
        if res is None:
            return 0
        return res
    
    def select_chat(self, chat_id):
        sql = """
        SELECT * FROM Chats WHERE chat_id = ?"""
        res = self.execute(sql=sql, parameters=(chat_id,), fetchone=True)
        if res is None:
            return 0
        return res