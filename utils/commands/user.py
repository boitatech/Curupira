from ..database.setup import User


def register_user(userID):
    # Cadastrar usuário no banco de dados
    try:
        user_registered = User(discordId=userID, score=0)
        user_registered.save()

    except Exception as err:
        print(err)

    return f"O usuário <@{userID}> foi cadastrado"
