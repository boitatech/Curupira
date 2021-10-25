

# def generate_database(conn):
#     cur = conn.cursor()

#     users = """
#             CREATE TABLE IF NOT EXISTS user (
#                 id serial primary key,
#                 discordId TEXT,
#                 score int,
#             )
#             """

#     cur.execute(users)
#     conn.commit()

#     challenges = """
#                 CREATE TABLE IF NOT EXISTS challenge (
#                     id serial primary key,
#                     description TEXT,
#                     flag TEXT,
#                     name TEXT,
#                     points int,
#                     category TEXT,
#                     level int,
#                     url TEXT
#                 )
#                 """

#     cur.execute(challenges)
#     conn.commit()

#     attemps = """
#                 CREATE TABLE IF NOT EXISTS attempt (
#                     id serial primary key,
#                     user_id int references user,
#                     chall_id int references challenge
#                 )
#               """

#     cur.execute(attemps)
#     conn.commit()


# def get_user_ranking(conn):
#     cur = conn.cursor()
#     users = f"""
#                 SELECT * FROM users LIMIT 10
#              """
#     pass


# def get_challenge_description(conn, challId):
#     cur = conn.cursor()
#     description = f"""
#                       SELECT description FROM challenge WHERE id == {challId}
#                    """

#     cur.execute(description)
#     data = cur.fetchall()
#     return data[0][0]
