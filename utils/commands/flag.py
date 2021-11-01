import utils.logging.log as log

from ..database.setup import Attempt, Challenge


def check_flag(challId, flag, userId):
    """
    Essa funcao verifica se a flag esta correta, criando sempre um Attempt

    @Params
    :challId => ID da Challenge
    :flag => flag do Challenge
    :userId => ID do Usuario
    """
    print("------> Vai procurar se o user ja fez a chall")
    try:
        Attempt.get(Attempt.correct == True, Attempt.user_id == userId, Attempt.chall_id == challId)
        return "Você já submeteu a flag desse desafio!"
    except Exception as e:
        log.err(e)

    print("------> Terminou de se o user ja fez a chall")

    log.debug("Vai procurar challenge")
    try:
        challInfo = Challenge.get_by_id(challId)
    except Exception as e:
        log.debug("Erro: " + e)
        return "Esse challenge id não existe!"
    print(f"------> Terminou de procurar challenge: {challInfo} {challInfo.flag}")

    print("------> Vai criar attempt")
    createAttempt = Attempt(
            user_id=userId,
            chall_id=challId,
            flag=flag,
            correct=challInfo.flag == flag
        )
    createAttempt.save()

    print("------> Terminou de criar attempt")

    if challInfo.flag == flag:
        return f"Parabéns!!! Você resolveu o desafio {challInfo.name}!"

    return "Flag incorreta!"


# a = Attempt.select(Attempt.flag)
# result = [i for i in a]
