from ..database.setup import Attempt, Challenge
from datetime import datetime
<<<<<<< HEAD
from peewee import DoesNotExist
from utils.logging.log import log
=======
>>>>>>> ec7541ae5ae3f65a1f720c50127a30c74eccc70e


def check_flag(challId, flag, userId):
    """
    Essa funcao verifica se a flag esta correta, criando sempre um Attempt

    @Params
    :challId => ID da Challenge
    :flag => flag do Challenge
    :userId => ID do Usuario
    """
    log.debug("Vai procurar se o user ja fez a chall")
    try:
        Attempt.get(Attempt.correct == True, Attempt.user_id == userId, Attempt.chall_id == challId)
        return "Você já submeteu a flag desse desafio!"
<<<<<<< HEAD
    except DoesNotExist as e:
        log.err(e)
=======
    except Exception as e:
        print(e)
>>>>>>> ec7541ae5ae3f65a1f720c50127a30c74eccc70e

    log.debug("Terminou de se o user ja fez a chall")

<<<<<<< HEAD
    log.debug("Vai procurar challenge")
=======
    print("------> Vai procurar challenge")

>>>>>>> ec7541ae5ae3f65a1f720c50127a30c74eccc70e
    try:
        challInfo = Challenge.get_by_id(challId)
    except IndexError:
        return "Esse challenge id não existe!"
    log.debug("Terminou de procurar challenge")

    log.debug("Vai criar attempt")
    Attempt.create(
            user_id=userId,
            chall_id=challId,
            flag=flag,
            correct=challInfo.flag == flag,
            timestamp=datetime.timestamp(datetime.now())
        )
    log.debug("Terminou de criar attempt")

    if challInfo.flag == flag:
        return f"Parabéns!!! Você resolveu o desafio {challInfo.name}!"

    return "Flag incorreta!"


# a = Attempt.select(Attempt.flag)
# result = [i for i in a]
