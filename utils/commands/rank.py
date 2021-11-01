from utils.logging.log import log
from ..database.setup import User, Attempt


def get_ranking_with_user(ctx):
    try:
        users = (
            User.select()
            .join(Attempt)
            .having(Attempt.user_id == User.discordId)
            .having(Attempt.correct)
            .order_by(User.score.desc())
            .order_by(Attempt.timestamp.desc())
            )

        ranking = ""
        for idx, user in enumerate(users.iterator()):
            ranking += f'''#{idx} <@{user.discordId}> - {user.score}
---------------------------------------
'''
        return ranking

    except Exception as err:
        log.err(err)
