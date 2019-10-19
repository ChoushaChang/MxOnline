#!/usr/bin/env python
# -*- coding: utf-8 -*-

#set up
import sys
import os
from youtubedata import cate
pwd=os.path.abspath(os.path.join(os.path.dirname('Org_Input.py'),os.path.pardir))
sys.path.append(pwd)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxOnline.settings")

import django
django.setup()

#import models
from apps.organizations.models import CourseOrg
from apps.courses.models import Course,Lesson,Video,CourseTag
from MxOnline.settings import MEDIA_URL,MEDIA_ROOT

#import csv
import csv
import pandas as pd

VideoCSV = pd.read_csv("course_cate.csv")
channel_csv = pd.read_csv("channel_df2.csv")

cate_df=cate()
cate_values_list=list(cate_df.values())
# print(cate_values_list)
org_df=pd.DataFrame(channel_csv)
        

def OrgInput():
    for i in range(len(channel_csv)):
        if len(CourseOrg.objects.filter(name=org_df['ChannelTitle'][i])) <= 0:
            courseorg = CourseOrg.objects.create(
                name=org_df['ChannelTitle'][i],
                desc=org_df['Channel_desc'][i],
                click_nums=org_df['Clicknums'][i],
                fav_nums=org_df['fav_nums'][i],
                image=org_df['image_url'][i],
                course_nums=org_df['video_numb'][i],
            )
            print("insert successed!!")
        else:
            print("error!"+"data in {}".format(i)+" line")
#OrgInput()
def CourseInput():
    for j in range(len(VideoCSV)):
        c_org_name=VideoCSV['channelTitle'][j]
        course = Course.objects.create(
            course_org = CourseOrg.objects.get_or_create(name=c_org_name)[0],
            name = VideoCSV['title'][j],
            detail = VideoCSV['desc'][j],
            fav_nums = VideoCSV['likeCount'][j],
            category = VideoCSV['category'][j],
            click_nums = VideoCSV['viewCount'][j],
            image = VideoCSV['thumbnails_url'][j],   
        )
        lesson = Lesson.objects.create(
            course = Course.objects.get(name=VideoCSV['title'][j]),
            name = VideoCSV['title'][j],
        )
        video = Video.objects.create(
            lesson = Lesson.objects.get(name=VideoCSV['title'][j]),
            name = VideoCSV['title'][j],
            url = VideoCSV['video_url'][j],
        )
#CourseInput()

def CourseComment():
    v_comment=VideoCSV['tags']
    for k in range(len(VideoCSV)):
        temp=v_comment[k][1:-1].split(',')
        for ch in temp:
            coursetag = CourseTag.objects.create(
                course=Course.objects.get(name=VideoCSV['title'][k]),
                tag=ch.strip()[1:-1]
            )
#CourseComment()
