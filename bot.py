# bot.py

import discord
from discord.ext import commands
from dotenv import load_dotenv

import sqlite3
from sqlite3 import Error


from utils.commands.rank import get_ranking_with_user
from utils.commands.flag import check_flag
from utils.database.setup import get_challenge_description

import os


# Boring config
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
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


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('Boitatech CTF'))
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))


if __name__ == "__main__":
    # TODO: instanciar banco de dados
    CONN = None
    try:
        CONN = sqlite3.connect("./utils/database/database.sqlite")
    except Error as e:
        print(e)
    bot.run(TOKEN)
