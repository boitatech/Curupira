import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def generate_database(conn):
    users = """
            CREATE TABLE user (
                id serial primary key,
                discordId TEXT
            )
            """

    challenges = """
                CREATE TABLE challenge (
                    id serial primary key,
                    description TEXT,
                    flag TEXT,
                    name TEXT,
                    points int,
                    category TEXT,
                    level int,
                    url TEXT
                )
                """
    
    attemps = """
                CREATE TABLE attempt (
                    id serial primary key,
                    user_id int references user,
                    chall_id int references challenge
                )
              """

    cur = conn.cursor()
    cur.execute(users)
    conn.commit()
    cur.execute(challenges)
    conn.commit()
    cur.execute(attemps)
    conn.commit()

def register_attempt(conn):
    pass
