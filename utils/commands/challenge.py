from ..database.setup import Challenge, Attempt, User
import utils.logging.log as log
import discord


def get_challenges(ctx):
    """
    Essa funcao retorna todos os challenges cadastrados no CTF
    """
    try:
        user = User.get(User.discordId == ctx.author.id)
    except Exception as e:
        log.err(e)
        return discord.Embed(title="Registre-se!", description="Você não está cadastrado, use o comando $register para se cadastrar!") 

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
        return discord.Embed(title="Challenges", description=challs)
    except Exception as err:
        log.err(err)
