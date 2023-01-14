from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")

HOST_DB = env.str('HOST_DB')
PORT_DB = env.int('PORT_DB')
USER_DB = env.str('USER_DB')
PASSWORD_DB = env.str('PASSWORD_DB')
NAME_DB = env.str('NAME_DB')
