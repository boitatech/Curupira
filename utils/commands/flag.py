from ..database.setup import Attempt, Challenge
from datetime import datetime


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
        print(f"DEU MERDA AQUI: {e}")

    print("------> Terminou de se o user ja fez a chall")

    print("------> Vai procurar challenge")

    try:
        challInfo = Challenge.get_by_id(challId)
    except IndexError:
        return "Esse challenge id não existe!"
    print(f"------> Terminou de procurar challenge: {challInfo}")

    print("------> Vai criar attempt")
    Attempt.create(
            user_id=userId,
            chall_id=challId,
            flag=flag,
            correct=challInfo.flag == flag,
            timestamp=datetime.timestamp(datetime.now())
        )
    print("------> Terminou de criar attempt")

    if challInfo.flag == flag:
        return f"Parabéns!!! Você resolveu o desafio {challInfo.name}!"

    return "Flag incorreta!"


# a = Attempt.select(Attempt.flag)
# result = [i for i in a]
