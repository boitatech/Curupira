from ..database.setup import User
from utils.logging.log import log


def register_user(userID):
    # Cadastrar usuário no banco de dados
    try:
        user_registered = User(discordId=userID, score=0)
        user_registered.save()
        return f"O usuário <@{userID}> foi cadastrado!"

    except Exception as err:
        log.err(err)
        return f'<@{userID}> já foi cadastrado! Faça os desafios agora!'
  