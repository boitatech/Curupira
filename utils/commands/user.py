from ..database.setup import User
import utils.logging.log as log


def register_user(ctx, userID):
    """
    Essa funcao registra um usuario no banco de dados do CTF

    @Params
    :userID => Id da conta do Discord
    """
    user = User.get_or_none(User.discordId == ctx.author.id)
    if user is not None:
        return f'<@{userID}> já foi cadastrado! Faça os desafios agora!'
    try:
        user_registered = User(discordId=userID, score=0)
        user_registered.save()
        return f"O usuário <@{userID}> foi cadastrado!"

    except Exception as err:
        log.err(err)
        return f'<@{userID}> já foi cadastrado! Faça os desafios agora!'
