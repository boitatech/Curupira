import utils.logging.log as log

from ..database.setup import Attempt, Challenge, User
import peewee
from datetime import datetime


def check_flag(challId, flag, discordId):
    """
    Essa funcao verifica se a flag esta correta, criando sempre um Attempt

    @Params
    :challId => ID da Challenge
    :flag => flag do Challenge
    :userId => ID do Usuario
    """
    try:
        user = User.get(User.discordId == discordId)
    except:
        return "Você não está cadastrado, use o comando $register para se cadastrar!"

    try:
        chall = Challenge.get_by_id(challId)
    except Exception as e:
        log.err(e)
        return "Esse challenge id não existe!"

    try:
        Attempt.get(Attempt.correct == True, Attempt.user_id == user.id, Attempt.chall_id == challId)
        return "Você já submeteu a flag desse desafio!"
    except peewee.DoesNotExist as e:
        log.err(e)

    print(chall.flag)
    print(flag)

    print(user.score)
    print(chall.points)
    score = user.score + chall.points
    if chall.flag == flag:
        try:
            Attempt.create(user_id=user.id, chall_id=challId, flag=flag, correct=True, timestamp=datetime.timestamp(datetime.now()))
            User.update(score=score, last_submit=datetime.timestamp(datetime.now())).where(User.discordId == discordId).execute()
            return "Flag correta!"
        except Exception as e:
            log.err(e)
            return "Erro ao criar Attempt True"
    else:
        try:
            Attempt.create(user_id=user.id, chall_id=challId, flag=flag, correct=False, timestamp=datetime.timestamp(datetime.now()))
            return "Flag incorreta!"
        except Exception as e:
            log.err(e)
            return "Erro ao criar Attempt False"



# a = Attempt.select(Attempt.flag)
# result = [i for i in a]
