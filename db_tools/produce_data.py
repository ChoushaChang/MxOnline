import os,sys
from tqdm import tqdm
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxOnline.settings")
pwd=os.path.abspath(os.path.join(os.path.dirname('produce_data.py'),os.path.pardir))
sys.path.append(pwd)

import django
django.setup()

#import models
from apps.organizations.models import CourseOrg
from apps.courses.models import Course,Lesson,Video,CourseTag
from MxOnline.settings import MEDIA_URL,MEDIA_ROOT

#import csv
import csv
import pandas as pd

VideoCSV = pd.read_csv("./data_csv/course_cate.csv")
channel_csv = pd.read_csv("./data_csv/channel_df2.csv")
org_df=pd.DataFrame(channel_csv)

def OrgInput():
    for i in tqdm(range(len(channel_csv))):
        if len(CourseOrg.objects.filter(name=org_df['ChannelTitle'][i])) <= 0:
            courseorg = CourseOrg.objects.create(
                name=org_df['ChannelTitle'][i],
                desc=org_df['Channel_desc'][i],
                click_nums=org_df['Clicknums'][i],
                fav_nums=org_df['fav_nums'][i],
                image=org_df['image_url'][i],
                course_nums=org_df['video_numb'][i],
            )
        else:
            print("error!"+"data in {}".format(i)+" line")

def CourseInput():
    for j in tqdm(range(len(VideoCSV))):
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

def CourseTags():
    v_comment=VideoCSV['tags']
    for k in tqdm(range(len(VideoCSV))):
        temp=v_comment[k][1:-1].split(',')
        for ch in temp:
            coursetag = CourseTag.objects.create(
                course=Course.objects.get(name=VideoCSV['title'][k]),
                tag=ch.strip()[1:-1]
            )

def delete_db():
    print('truncate db')
    CourseOrg.objects.all().delete()
    Course.objects.all().delete()
    Lesson.objects.all().delete()
    Video.objects.all().delete()
    CourseTag.objects.all().delete()
    print('finished truncate db')

if __name__ == '__main__':
    print("Starting  Data script...")
    delete_db()
    OrgInput()
    CourseInput()
    CourseTags()
    print("Finished!!")