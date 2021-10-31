from ..database.setup import Challenge


def get_challenges():
    # pega todas as challs
    try:
        challenges = Challenge.select()
        for challenge in challenges:
            print(challenge.name)
            return """{challenge.name}, {challenge.points} Pontos - {challenge.category}
            {challenge.description}
            {challenge.url}
            ------------------------------------------------------------"""

    except Exception as err:
        print(err)