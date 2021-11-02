import discord
import utils.logging.log as log

from discord.ext import commands
from utils.config import TOKEN
from utils.commands.rank import get_ranking_top_ten
from utils.commands.flag import check_flag
from utils.database.setup import get_challenge_description, init_database
from utils.commands.user import register_user
from utils.commands.challenge import get_challenges
# Database setup
# http://docs.peewee-orm.com/en/latest/peewee/quickstart.html


bot = commands.Bot(command_prefix='$', description="Boitatech CTF")

bot.remove_command("help")

@bot.command()
async def test(ctx, *, arg):
    await ctx.send(ctx)


@bot.command()
async def ranking(ctx):
    """
    Esse comando pega os top 10 usuários no ranking
    e dá a posição atual da pessoa que chamou o comando.
    """
    await ctx.send(embed=get_ranking_top_ten())


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
                await ctx.send(check_flag(challId, flag, ctx.author.id))
            else:
                await ctx.author.dm_channel.send("Você precisa mandar uma `challId` e uma `flag`!")
        except Exception as err:
            log.err(err)
    else:
        await ctx.message.delete()
        await ctx.author.dm_channel.send("Utilize o comando `$solve` aqui!")


@bot.command()
async def get_description(ctx, challId=None):
    """
    Esse comando deve trazer a descricao de uma chall.

    @Params
    :challId => Id da challenge
    """
    log.debug(challId)
    await ctx.send(get_challenge_description(challId))


@bot.command()
async def flag(ctx):
    """
    blablabla
    """
    await ctx.send(check_flag(ctx.message.id, ctx, ctx.author.id))


@bot.command()
async def register(ctx):
    """
    Registra o usuário
    """
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) == '\N{White Heavy Check Mark}'

    message = await ctx.send("\nGostaria de se registrar no CTF?")
    symbols = ['\N{White Heavy Check Mark}', '\N{Cross Mark}']
    for symbol in symbols:
        await message.add_reaction(symbol)
    await bot.wait_for('reaction_add', timeout=60.0, check=check)
    await ctx.send(register_user(ctx.author.id))


@bot.command()
async def challs(ctx):
    """
    Mostras as challs
    """

    await ctx.send("\n============== CHALLENGES ==============")
    await ctx.send(embed=get_challenges())

@bot.group(invoke_without_command=True)
async def help(ctx):
    """
    Cria novo help custom
    """
    a = discord.Embed(title="Boitatech CTF", colour=0xFF0000)
    a.add_field(name="Help", value="Use $help [comando] para uma informação mais detalhada")
    a.add_field(name="Comandos Disponiveis", value="""
solve
ranking
register
help
get_description""")
    await ctx.send(embed=a)


@help.command()
async def solve(ctx):
    """
    para $help comando
    """
    b = discord.Embed(title="Resolver challenge", description="O formato que a flag deve ser inputado deve ser toda a string, incluindo bCTF\{\}", colour=0xFF0000)
    b.add_field(name="Sintaxe", value="$solve [id_challenge] [flag]")
    await ctx.send(embed=b)


@help.command()
async def ranking(ctx):
    b = discord.Embed(title="Checar ranking", description="O comando retorna os 10 primeiros no ranking e o ranking do usuário atual registrado.", colour=0xFF0000)
    b.add_field(name="Sintaxe", value="$ranking")
    await ctx.send(embed=b)


@help.command()
async def register(ctx):
    b = discord.Embed(title="Registrar usuário", description="O comando register registra o usuário do discord atual automaticamente no Boitatech CTF", colour=0xFF0000)
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
