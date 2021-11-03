from ..database.setup import User
import utils.logging.log as log
import discord


def get_ranking_top_ten(ctx):
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
        currentUser = User.select().order_by(User.score.desc(), User.last_submit.asc()).where(User.discordId == ctx.author.id).first()
        embed = discord.Embed(title="Ranking", description=ranking)
        embed.set_footer(text=f'Sua posição é #{currentUser}' if currentUser else 'Registre-se digitando $register')
        return embed
    except Exception as err:
        log.err(err)
