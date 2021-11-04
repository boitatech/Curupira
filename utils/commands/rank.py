from ..database.setup import User, _DB
import utils.logging.log as log
import discord
import peewee


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
        rank_expr = peewee.fn.rank().over(order_by=[User.score.desc(), User.last_submit.asc()])
        subquery = User.select(User.discordId, rank_expr.alias('rank'))
        user_rank = peewee.Select(columns=[subquery.c.discordId, subquery.c.rank]).from_(subquery).where(subquery.c.discordId == str(ctx.author.id)).bind(_DB).first()
        embed = discord.Embed(title="Ranking", description=ranking)
        embed.set_footer(text=f'Sua posição é #{user_rank["rank"]}' if user_rank else 'Registre-se digitando $register')
        return embed
    except Exception as err:
        log.err(err)
