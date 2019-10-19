#!/usr/bin/env python
# -*- coding: utf-8 -*-

#set up
import sys
import os

pwd=os.path.abspath(os.path.join(os.path.dirname('Org_Input.py'),os.path.pardir))
sys.path.append(pwd)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxOnline.settings")

import django
django.setup()

#import models
from apps.organizations.models import CourseOrg,Teacher
from apps.courses.models import Course,Lesson,Video

#import csv
import csv
import pandas as pd

VideoCSV = pd.read_csv("video_db.csv")
#test channel_title
print(VideoCSV.head())
channel_title_list=[]
channel_title_list=list(VideoCSV['channel_title'])
print(len(channel_title_list))
print(channel_title_list)

def CourseInput():
    course_title_list=[]
    Video_list=[]
    course_title_list=list(VideoCSV['title'])
    thumbnail_link=list(VideoCSV['thumbnail_link'])
    des=list(VideoCSV['description'])
    Views=list(VideoCSV['views'])
    VideoId=list(VideoCSV['video_id'])
    Videourl_list=(VideoCSV['VideoUrl'])
    j=3
    for i in range(len(course_title_list)):
        course=Course.objects.create(teacher=Teacher.objects.get(id=1),course_org=CourseOrg.objects.get(id=1),name=course_title_list[i],desc=des[i],click_nums=Views[i],image=thumbnail_link[i])
CourseInput()
