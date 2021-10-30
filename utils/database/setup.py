from peewee import SqliteDatabase, TextField, IntegerField, Model
from peewee import ForeignKeyField, AutoField


def init_database():
    print('Iniciando DB...')
    _DB = None
    _DB = SqliteDatabase('./database.sqlite')
    _DB.connect()
    _DB.create_tables([Challenge], safe=True)
    _DB.create_tables([User], safe=True)
    _DB.create_tables([Attempt], safe=True)
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


def get_challenge_description(challId):
    test = Challenge.select(
                            Challenge.description
                           ).where(
                            Challenge.id == challId
                           )

    import ipdb
    ipdb.set_trace()
    return test
