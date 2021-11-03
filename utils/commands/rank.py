from ..database.setup import User, Attempt, Challenge, _DB
import utils.logging.log as log
import discord
import peewee
import plotly.express as px


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

async def get_ranking_chart(bot):
    top10 = (
        User.select(User.discordId)
            .order_by(User.score.desc(), User.last_submit.asc())
            .limit(10)
    )
    cumulative_expr = peewee.fn.SUM(Challenge.points).over(partition_by=[User.discordId], order_by=[Attempt.timestamp])
    attempts = Attempt.select(User.discordId, Attempt.timestamp, Challenge.points, cumulative_expr.alias('cum_points')).join(Challenge, on=(Challenge.id == Attempt.chall_id)).join(User, on=(User.id == Attempt.user_id)).where(User.discordId << top10, Attempt.correct).order_by(Attempt.timestamp.asc())
    attempts = tuple([await get_usernames(attempt, bot) for attempt in attempts.dicts()])
    fig = px.line(attempts, x="timestamp", y="cum_points", color="user", labels={'timestamp': 'Tempo', 'cum_points': 'Pontos', 'user': 'usuário'})
    return fig.to_image(format="png", width=200, height=200, scale=1)

async def get_usernames(attempt, bot):
    attempt['user'] = await bot.fetch_user(attempt['discordId'])
    return attempt
