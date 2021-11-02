from ..database.setup import User
import utils.logging.log as log
import discord


def get_ranking_top_ten():
    """
    Essa funcao retorna os top 10 colocados no CTF
    """
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
