import os

from environs import Env


env = Env()


ROOT = os.path.dirname(os.path.abspath(__file__))

BASE_DIR = os.path.dirname(os.path.dirname(ROOT))
env_file = os.path.join(BASE_DIR, '.env')



if os.path.exists(env_file):
    env.read_env(env_file)

TOKEN = env('DISCORD_TOKEN')
ENV = env('ENV')
