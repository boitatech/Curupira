from ..database.setup import User
from utils.logging.log import log


def get_ranking_with_user(ctx):
    try:
        users = User.select()
        ranking = ""
        for user in users.iterator(): #users[0].discordId
            ranking += f'''#1 <@{user.discordId}> - {user.score}
------------------------------------------------------------
'''
        return ranking

    except Exception as err:
        log.err(err)
