import discord
from time import sleep
import utils.logging.log as log

from discord.ext import commands
from utils.config import TOKEN
from utils.commands.rank import get_ranking_top_ten
from utils.commands.flag import check_flag
from utils.database.setup import get_challenge_description, init_database
from utils.commands.user import register_user
from utils.commands.challenge import get_challenges

# http://docs.peewee-orm.com/en/latest/peewee/quickstart.html


bot = commands.Bot(command_prefix='$', description="$help + Boitatech CTF")

bot.remove_command("help")


@bot.command()
async def ranking(ctx):
    """
    Esse comando pega os top 10 usuários no ranking
    e dá a posição atual da pessoa que chamou o comando.
    """
    try:
        await ctx.send(embed=get_ranking_top_ten(ctx))
    except Exception as err:
        log.err(err)


@bot.command()
async def solve(ctx, challId=None, flag=None):
    """
    Esse comando inputa uma flag

    :challId = Id da challenge
    :flag = Flag pra dar input
    """
    await ctx.author.create_dm()
    if isinstance(ctx.channel, discord.channel.DMChannel):
        try:
            if challId and flag:
                if len(challId) < 420 and len(flag) < 420:
                    if challId.isnumeric():
                        await ctx.send(embed=check_flag(ctx, challId, flag, ctx.author.id))
                    else:
                        await ctx.author.dm_channel.send("`challId` precisa ser um número!")
                else:
                    await ctx.author.dm_channel.send("Você precisa mandar uma `challId` e uma `flag`!")
        except Exception as err:
            log.err(err)
    else:
        await ctx.message.delete()
        await ctx.author.dm_channel.send("Utilize o comando `$solve` aqui!")


@bot.command()
async def register(ctx):
    """
    Registra o usuário
    """
    if isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.author.create_dm()
        await ctx.send('Utilize o comando `$register` no servidor do Boitatech')
    else:
        def check(reaction, user):
            return user == ctx.author and (str(reaction.emoji) == '\N{Cross Mark}' or str(reaction.emoji) == '\N{White Heavy Check Mark}')

        userID = ctx.author.id
        message = await ctx.send(f'<@{userID}> gostaria de se registrar?')

        symbols = ['\N{White Heavy Check Mark}', '\N{Cross Mark}']
        for symbol in symbols:
            await message.add_reaction(symbol)
        reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
        if reaction.emoji == '\N{White Heavy Check Mark}':
            await ctx.send(register_user(ctx, userID))
            await ctx.message.delete()
            await message.delete()
        elif reaction.emoji == '\N{Cross Mark}':
            await ctx.message.delete()
            await message.delete()


@bot.command()
async def challs(ctx):
    """
    Mostras as challs
    """
    await ctx.author.create_dm()
    if not isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.message.delete()
    challs = get_challenges(ctx)
    print(challs)
    print("*" * 80)
    print(type(challs))
    for chall in challs:
        await ctx.author.dm_channel.send(embed=chall)


# ================
# MOCK HELP STUFF
# ================


@bot.group(invoke_without_command=True)
async def help(ctx):
    """
    Cria novo help custom
    """
    a = discord.Embed(title="Boitatech CTF", colour=0xFF0000)
    a.add_field(name="Help", value="Use $help [comando] para mais informações!")
    a.add_field(name="Comandos Disponiveis", value="""
                                                      register
                                                      solve
                                                      challs
                                                      ranking
                                                    """)
    await ctx.send(embed=a)


@help.command()
async def solve(ctx):
    """
    Mock p/ $help
    """
    b = discord.Embed(title="Resolver challenge", description="O formato que a flag deve ser inputado deve ser toda a string, incluindo bCTF\{\}", colour=0xFF0000)
    b.add_field(name="Sintaxe", value="$solve [id_challenge] [flag]")
    await ctx.send(embed=b)


@help.command()
async def ranking(ctx):
    """
    Mock p/ $help
    """
    b = discord.Embed(title="Checar ranking", description="O comando retorna os 10 primeiros no ranking e o ranking do usuário atual registrado.", colour=0xFF0000)
    b.add_field(name="Sintaxe", value="$ranking")
    await ctx.send(embed=b)


@help.command()
async def challs(ctx):
    """
    Mock p/ $help
    """
    b = discord.Embed(title="Checar challs", description="O comando retorna ass challenges que você precisa fazer.", colour=0xFF0000)
    b.add_field(name="Sintaxe", value="$challs")
    await ctx.send(embed=b)


@help.command()
async def register(ctx):
    """
    Mock p/ $help
    """
    b = discord.Embed(title="Registrar usuário", description="O comando `register` dá a possibilidade de participar do Boitatech CTF", colour=0xFF0000)
    b.add_field(name="Sintaxe", value="$register")
    await ctx.send(embed=b)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('Boitatech CTF'))
    log.debug('Connected to bot: {}'.format(bot.user.name))
    log.debug('Bot ID: {}'.format(bot.user.id))


if __name__ == "__main__":
    init_database()
    bot.run(TOKEN)
