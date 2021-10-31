from peewee import PostgresqlDatabase, TextField, IntegerField, Model
from peewee import ForeignKeyField, AutoField
from peewee_async import Manager
from utils.config import DB_NAME, DB_USERNAME, DB_PASSWORD, DB_HOSTNAME
from utils.commands.user import register_user

def init_database():
    print('Iniciando DB...')
    _DB = None
    _DB = PostgresqlDatabase(
        DB_NAME,
        user=DB_USERNAME,
        password=DB_PASSWORD,
        host=DB_HOSTNAME
        )
    _DB.connect()
    return _DB


_DB = init_database()


class BaseModel(Model):
    class Meta:
        database = _DB


class Challenge(BaseModel):
    id = AutoField(primary_key=True)
    description = TextField()
    flag = TextField()
    name = TextField()
    points = IntegerField()
    category = TextField()
    level = IntegerField()
    url = TextField()


class User(BaseModel):
    id = AutoField(primary_key=True)
    descordId = TextField()
    score = IntegerField()


class Attempt(BaseModel):
    id = AutoField(primary_key=True)
    user_id = ForeignKeyField(User, backref='user')
    chall_id = ForeignKeyField(Challenge, backref='challenge')


_DB.create_tables([Challenge], safe=True)
_DB.create_tables([User], safe=True)
_DB.create_tables([Attempt], safe=True)


def get_challenge_description(challId):
    test = Challenge.select(
                            Challenge.description
                           ).where(
                            Challenge.id == challId
                           )

    return test
