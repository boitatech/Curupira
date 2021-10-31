from ..database.setup import Challenge


def get_challenges():
    # pega todas as challs
    try:
        challenges = Challenge.select(
            Challenge.id,
            Challenge.name, 
            Challenge.points, 
            Challenge.category, 
            Challenge.description,
            Challenge.url
            )
        for challenge in challenges:
            return f'''{challenge.name} {challenge.id}, {challenge.points} Pontos - {challenge.category}
            {challenge.description}
            {challenge.url}
            ------------------------------------------------------------'''

    except Exception as err:
        print(err)