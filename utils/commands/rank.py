import utils.logging.log as log
from ..database.setup import User, Attempt


def get_ranking_with_user(ctx):
    try:
        users = (
            User.select()
            .order_by(User.score.desc())
            .order_by(User.last_submit.desc())
            )

        ranking = ""
        for idx, user in enumerate(users.iterator()):
            ranking += f'#{idx} <@{user.discordId}> - {user.score}\n'
        return discord.Embed(title="Ranking", description=ranking)

    except Exception as err:
        log.err(err)
