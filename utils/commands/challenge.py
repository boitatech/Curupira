from ..database.setup import Challenge


def get_challenges(userID):
    # Cadastrar usuário no banco de dados
    try:
        challenges = Challenge.select()
        return challenges

    except Exception as err:
        print(err)