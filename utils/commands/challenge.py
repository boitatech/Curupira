from ..database.setup import Challenge, Attempt, User
import utils.logging.log as log
import discord


async def get_challenges(ctx):
    """
    Essa funcao retorna todos os challenges cadastrados no CTF
    """
    user = User.get_or_none(User.discordId == ctx.author.id)
    if user is None:
        return discord.Embed(title="Regitre-se", description="Use $register para se registrar")
    else:
        try:
            user = User.get(User.discordId == ctx.author.id)

            challenges = Challenge.select(
                                        Challenge.id,
                                        Challenge.name,
                                        Challenge.points,
                                        Challenge.category,
                                        Challenge.description,
                                        Challenge.url
                                        )

            attempts = Attempt.select(Attempt.chall_id).where(Attempt.correct == True, Attempt.user_id == user.id)

            challs = ""

            for challenge in challenges:
                _banned_ids = []
                if len(attempts) >= 1:
                    for attempt in attempts:
                        if challenge.id == attempt.chall_id_id:
                            _banned_ids.append(challenge.id)

                if challenge.id not in _banned_ids:
                    challs += f'''
                                **[ID: {challenge.id}] - {challenge.name}**
                                [CATEGORY] - {challenge.category}
                                [PONTOS] - {challenge.points}
                                [DESCRIPTION] - {challenge.description}
                                [+] {challenge.url}
                                {"-" * 64}
                            '''
                    if len(challs) > 650:
                        await ctx.author.dm_channel.send(challs)
                        challs = "."
            await ctx.author.dm_channel.send(challs)
        except Exception as err:
            log.err(err)
