from decouple import config
from uuid import uuid4
from datetime import datetime
import random

REDIS_PORT = config("REDIS_PORT")
REDIS_HOST = config("REDIS_HOST")
REDIS_PASSWORD = config("REDIS_PASSWORD")
SUCESSFUL = 200;
NOT_FOUND = 404;
FORBIDEEN = 403;
CRASH = 503;
SUCESSFUL_MSG = "sucessful";
NOT_FOUND_MSG = "not found";
FORBIDEEN_MSG = "request forbidden";
CRASH_MSG = "unexpected issue";

def get_uid(): return str(uuid4().hex)

def get_random_integer_string():
    random_integers = [str(random.randint(0, 9)) for _ in range(5)]
    return ''.join(random_integers)

def generate_random_code(length=6): return ''.join(random.choices('0123456789', k=length))

def get_current_date(): return datetime.today().strftime('%Y-%m-%d %H:%M:%S')