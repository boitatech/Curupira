from ..database.setup import User


def register_user(userID):
    # Cadastrar usuário no banco de dados
    try:
        user_registered = User(discordId=userID, score=0)
        user_registered.save()
        return f"O usuário <@{userID}> foi cadastrado!"

    except Exception as err:
        print(err)
        return f'<@{userID}> já foi cadastrado! Faça os desafios agora!'