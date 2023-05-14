import os


class Config(object):
    SECRET_KEY = os.environ('SECRET_KEY') or 'you-will-never-guess'