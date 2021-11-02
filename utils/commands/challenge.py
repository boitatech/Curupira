from ..database.setup import Challenge, Attempt, User
import utils.logging.log as log
import discord


def get_challenges(ctx):
    """
    Essa funcao retorna todos os challenges cadastrados no CTF
    """
    try:
        user = User.get(User.discordId == ctx.author.id)
        challenges = Challenge.select(Challenge.id,
                                      Challenge.name, 
                                      Challenge.points, 
                                      Challenge.category, 
                                      Challenge.description,
                                      Challenge.url)
        
        attempts = Attempt.select(Attempt.chall_id).where(Attempt.correct == True, Attempt.user_id == user.id)
        

        # Filtrar os attempts corrects do user
        #
        #
        challs = ""
        for challenge in challenges.iterator():
            for attempt in attempts.iterator():
                if challenge.id == attempt.chall_id:
                     challenges.pop(challenge)
            challs += f'''{challenge.name} ({challenge.id}) - {challenge.points} Pontos - {challenge.category}
                          {challenge.description}
                          {challenge.url}
                       ------------------------------------------------------------
                       '''
        return discord.Embed(title="Challeges", description=challs)
    except Exception as err:
        log.err(err)