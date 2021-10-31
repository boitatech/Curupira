from ..database.setup import Challenge


def get_challenges():
    # pega todas as challs
    try:
        challenges = Challenge.select()
        return challenges

    except Exception as err:
        print(err)