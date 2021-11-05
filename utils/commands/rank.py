from ..database.setup import User, _DB
import utils.logging.log as log
import discord
import peewee


def get_ranking_top_ten(ctx):
    """
    Essa funcao retorna a posicao do usuario
    """
    try:
        rank_expr = peewee.fn.rank().over(order_by=[User.score.desc(), User.last_submit.asc()])
        subquery = User.select(User.discordId, rank_expr.alias('rank'))
        user_rank = peewee.Select(columns=[subquery.c.discordId, subquery.c.rank]).from_(subquery).where(subquery.c.discordId == str(ctx.author.id)).bind(_DB).first()
        return user_rank
    except Exception as err:
        log.err(err)

def scoreboard():
    """
    Essa funcao edita a mensagem para o scoreboard
    """

    users = (
        User.select().order_by(User.score.desc(), User.last_submit.asc())
                        .limit(10)
    )
    ranking = "".join(
        f'#{idx+1} <@{user.discordId}> - {user.score}\n'
        for idx, user in enumerate(users.iterator())
    )
 
    channel = bot.get_channel(906198041814507541)
    message = channel.fetch_message(906201505793703967)

    message.edit(content=ranking)
