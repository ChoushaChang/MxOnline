import os,sys
from tqdm import tqdm
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxOnline.settings")
pwd=os.path.abspath(os.path.join(os.path.dirname('produce_edu.py'),os.path.pardir))
sys.path.append(pwd)

import django
django.setup()

# import csv
import csv
import pandas as pd

VideoCSV = pd.read_csv("./data_csv/Edu_Videos.csv")

print(VideoCSV.shape,VideoCSV.describe)