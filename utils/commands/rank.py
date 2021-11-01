import utils.logging.log as log
from ..database.setup import User, Attempt


def get_ranking_top_ten():
    try:
        users = (
            User.select()
            .order_by(User.score.desc())
            .order_by(User.last_submit.desc())
            .limit(10)
            )

        ranking = ""
        for idx, user in enumerate(users.iterator()):
            ranking += f'''#{idx+1} <@{user.discordId}> - {user.score}
---------------------------------------
'''
        return ranking

    except Exception as err:
        log.err(err)
