def register_user(userId):
    # Cadastrar usuário no banco de dados
    user_registered = User(discordId=userId)
    user_registered.save()
