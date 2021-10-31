def register_user(userID):
    # Cadastrar usuário no banco de dados
    try:
        user_registered = User(discordId=userID)
        user_registered.save()
    
    except Exception as err:
        print(err)

    return "Seu usuário {} foi cadastrado".format(userID)
