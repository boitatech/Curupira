from ..database.setup import User, _DB


def get_ranking_with_user(ctx):
    data = _DB.execute(User.select(User.score).where(User.descordId == ctx.author.id))
    return data
    # mock = """\n
    #             RANKING: \n
    #         1º - Usuário 1
    #         2º - Usuário 2
    #         3º - Usuário 3
    #         4º - Usuário 4
    #         5º - Usuário 5
    #         6º - Usuário 6
    #         7º - Usuário 7
    #         8º - Usuário 8
    #         9º - Usuário 9
    #         10º - Usuário 10

    #         Sua posição é 16
    #        """
    # return mock
