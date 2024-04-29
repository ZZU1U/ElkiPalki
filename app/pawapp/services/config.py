import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

SERVER_URL = os.environ.get('SERVER_URL')
