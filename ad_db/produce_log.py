import os,sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxOnline.settings")
pwd=os.path.abspath(os.path.join(os.path.dirname('produce_log.py'),os.path.pardir))
sys.path.append(pwd)

import django
django.setup()

import datetime
import random

from apps.collector.models import Log

SEED = 0

def select_action(user):
    actions = {'genreView': 15, 'details': 50, 'moreDetails': 24, 'addToList': 10, 'learn': 1}

    return sample(actions)


def sample(dictionary):
    random_number = random.randint(0, 100)
    index = 0
    for key, value in dictionary.items():
        index += value

        if random_number <= index:
            return key