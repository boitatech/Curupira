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
        attempts = Attempt.select(Attempt.chall_id).where(Attempt.correct == True and Attempt.user_id == user.id)
        print('=====> terminou de pegar a attempt')

        challs = ""
        for challenge in challenges.iterator():
            if len(attempts) >= 1:
                for attempt in attempts.iterator():
                    print(f"<> <> <>Attempt: {attempt}")
                    if challenge.id == attempt.chall_id:
                        print('O USER JA FEZ A CHALL')
            challs += f'''{challenge.name} ({challenge.id}) - {challenge.points} Pontos - {challenge.category}
                          {challenge.description}
                          {challenge.url}
                       ------------------------------------------------------------
                       '''
            # for challenge in challenges.iterator()
        # )

        return discord.Embed(title="Challenges", description=challs)
    except Exception as err:
        log.err(err)