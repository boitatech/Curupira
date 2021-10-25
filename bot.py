# bot.py

import discord
from discord.ext import commands
from utils.config import TOKEN
from utils.commands.rank import get_ranking_with_user
from utils.commands.flag import check_flag
from utils.database.setup import get_challenge_description
from peewee import *


# Database setup
# http://docs.peewee-orm.com/en/latest/peewee/quickstart.html       
db = SqliteDatabase('config/database/database.sqlite')


class Challenge(Model):
    description = TextField()
    flag = TextField()
    name = TextField()
    points = IntegerField()
    category = TextField()
    level = IntegerField()
    url = TextField()
    class Meta:
        database = db


class User(Model):
    descordId = TextField()
    score = IntegerField()
    class Meta:
        database = db


class Attempt(Model):
    user_id = ForeignKeyField()

# class Pet(Model):
#     owner = ForeignKeyField(Person, backref='pets')
#     name = CharField()
#     animal_type = CharField()
#     class Meta:
#         database = db # this model uses the "people.db" database


db.connect()
bot = commands.Bot(command_prefix='$', description="Boitatech CTF")


@bot.command()
async def test(ctx, *, arg):
    await ctx.send(arg)


@bot.command()
async def ranking(ctx):
    """
    Esse comando pega os top 10 usuários no ranking
    e dá a posição atual da pessoa que chamou o comando.
    """
    await ctx.send(f"{get_ranking_with_user()}")


@bot.command()
async def solve(ctx, challId=None, flag=None):
    """
    Esse comando inputa uma flag

    :challId = Id da challenge
    :flag = Flag pra dar input
    """
    if challId and flag:
        await ctx.send(check_flag(challId, flag, ctx.author.id))
    else:
        await ctx.send("Você precisa mandar uma `challId` e uma `flag`!")


@bot.command()
async def get_description(ctx, challId=None):
    """
    Esse comando deve trazer a descricao de uma chall.

    :challId = Id da challenge
    """
    print(challId)
    await ctx.send(get_challenge_description(CONN, challId))


# @bot.event
# async def on_message(message):
#     if isinstance(message.channel, discord.channel.DMChannel): 
#         await message.channel.send('!') 


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('Boitatech CTF'))
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))


if __name__ == "__main__":
    CONN = None
    try:
        CONN = SqliteDatabase('config/database/database.sqlite')
    except Error as e:
        print(e)
    bot.run(TOKEN)
