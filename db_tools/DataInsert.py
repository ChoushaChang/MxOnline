#!/usr/bin/env python
# -*- coding: utf-8 -*-

#setup
import sys
import os

pwd2=os.path.abspath(os.path.join(os.path.dirname('Datainsert.py'),os.path.pardir))
sys.path.append(pwd2)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxOnline.settings")

import django
django.setup()

#import models
from apps.organizations.models import City, CourseOrg

#importcsv
import csv
import pandas as pd 

VideoCSV = pd.read_csv("NewYoutubeData.csv")
# print(VideoCSV.head())

# channel_title_list=[]
# channel_title_list=list(VideoCSV['channel_title'])
# print(len(channel_title_list))
#print(channel_title_list)

# faker
from faker import Faker
import random
fakegen = Faker("zh_CN")

fake_n = ""
fake_ctgs3 = ["语文", "数学", "英语", "政治", "历史", "地理", "科学", "教育"]
fake_ctgs2 = ["初级", "中级", "高级"]
fake_ctgs = ["实战", "练习", "小测"]

fake_istab = ["False", "True"]
fake_code = fakegen.ean8()
fake_desc = fakegen.text(max_nb_chars=150)
fake_addtime = fakegen.date(pattern="%Y-%m-%d")
rand_ctgs3 = random.choice(fake_ctgs3) + str(fake_n)

# fake_tag = fakegen.word()

# def fake_citydic(N = 5):
#     global fake_n
#     for entry in range(N):
#         intn = entry+4
#         fake_n = str(intn)
#         fake_province = fakegen.province()
#         fake_city = fakegen.city()
#         citydic = City.objects.create(desc = fake_province, name = fake_city)
#         global citydic_instance 
#         citydic_instance = City.objects.get(name = fake_city)
#         # fake_courseorg()
#         # fake_taecher()
#         # fake_ctg()
#         # fake_course()
#         intn = intn + 1


def course_org_input():
    global fake_orgcode
    fake_orgcode = fakegen.ean8()

    channel_title_list=[]
    channel_title_list=list(VideoCSV['channel_title'])

    for i in range(len(channel_title_list)):
        course_org_input = CourseOrg.objects.create(
            org_code = fake_orgcode, 
            city_name = citydic_instance, 
            name = fake_org, 
            desc = fake_desc, 
            category = rand_ctg, 
            click_nums = fake_click, 
            fav_nums = fake_fav, 
            address = fake_addr, 
            students = fake_stunum, 
            course_nums = fake_course_nums
        )


def fake_courseorg():
        global fake_orgcode
        fake_orgcode = fakegen.ean8()
        global fake_org
        fake_org = fakegen.company()
        fake_desc = fakegen.text(max_nb_chars=150)
        fake_ctg = ["pxjg", "gr", "gx"]
        rand_ctg = random.choice(fake_ctg)
        fake_click = random.randint(1,1000)
        fake_fav = random.randint(1,1000)
        fake_addr = fakegen.address()
        fake_stunum = random.randint(1,1000)
        fake_course_nums = random.randint(1,600)
        courseorg = CourseOrg.objects.create(org_code = fake_orgcode, city_name = citydic_instance, name = fake_org, 
        desc = fake_desc, category = rand_ctg, click_nums = fake_click, fav_nums = fake_fav, 
        address = fake_addr, students = fake_stunum, course_nums = fake_course_nums)

if __name__ == '__main__':
    print("data is loading")
    #fake_ctg(10)
    #fake_user(10)
    #fake_tags()
    #fake_citydic(10)
    course_org_input()
    print("done")
    print("win!")