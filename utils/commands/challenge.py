from ..database.setup import Challenge, Attempt, User
import utils.logging.log as log
import discord


def get_challenges(ctx):
    """
    Essa funcao retorna todos os challenges cadastrados no CTF
    """
    try:
        print('=====> vai pegar o user')
        user = User.get(User.discordId == ctx.author.id)
        print('=====> terminou de pegar o user')

        print('=====> vai pegar a challenge')
        challenges = Challenge.select(
                                    Challenge.id,
                                    Challenge.name,
                                    Challenge.points,
                                    Challenge.category,
                                    Challenge.description,
                                    Challenge.url
                                    )
        print('=====> terminou de pegar a challenge')

        print('=====> vai pegar a attempt')
        attempts = Attempt.select(Attempt.chall_id).where(Attempt.correct == True, Attempt.user_id == user.id)
        print('=====> terminou de pegar a attempt')

        challs = ""

        for challenge in challenges:
            _banned_ids = []
            if len(attempts) >= 1:
                print('O USER TEM ATTEMPT')
                for attempt in attempts:
                    if challenge.id == attempt.chall_id_id:
                        print(f"Challenges = {type(challenges)} = {challenges}")
                        print("&" * 30)
                        print(f"Challenge = {type(challenge)} = {challenge}")
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
