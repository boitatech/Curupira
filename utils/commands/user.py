from ..database.setup import User
import utils.logging.log as log


def register_user(userID):
    """
    Essa funcao registra um usuario no banco de dados do CTF

    @Params
    :userID => Id da conta do Discord
    """
    try:
        user_registered = User(discordId=userID, score=0)
        user_registered.save()
        return f"O usuário <@{userID}> foi cadastrado!"

    except Exception as err:
        log.err(err)
        return f'<@{userID}> já foi cadastrado! Faça os desafios agora!'
