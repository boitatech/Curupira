from ..database.setup import User


def get_ranking_with_user():
    try:
        users = User.select()
        ranking = ""
        for user in users.iterator(): #users[0].discordId
            ranking += f'''#1 <@{user.discordId}> - {user.score}
------------------------------------------------------------
'''
        return ranking

    except Exception as err:
        print(err)
