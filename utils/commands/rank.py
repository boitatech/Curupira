import utils.logging.log as log
import discord

from ..database.setup import User


def get_ranking_top_ten():
    try:
        users = (
            User.select()
            .order_by(User.score.desc(), User.last_submit.asc())
            .limit(10)
            )

        ranking = "".join(
            f'#{idx+1} <@{user.discordId}> - {user.score}\n'
            for idx, user in enumerate(users.iterator())
        )

        return discord.Embed(title="Ranking", description=ranking)

    except Exception as err:
        log.err(err)
