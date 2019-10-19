from django.db import models
from DjangoUeditor.models import UEditorField

from apps.users.models import BaseModel

from DjangoUeditor.models import UEditorField

class CourseOrg(BaseModel):
    name = models.CharField(max_length=50, verbose_name="機構名稱")
    desc = UEditorField(verbose_name="機構描述", width=600, height=300, imagePath="courses/ueditor/images/",
                         filePath="courses/ueditor/files/", default="")
    click_nums = models.BigIntegerField(default=0, verbose_name="點擊數")
    students = models.IntegerField(default=0, verbose_name="學習人數")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏數")
    image = models.CharField(max_length=1000, verbose_name=u"封面圖")
    course_nums = models.IntegerField(default=0, verbose_name="課程數")
    is_auth = models.BooleanField(default=False, verbose_name="是否認證")
    is_gold = models.BooleanField(default=False, verbose_name="是否金牌")

    def courses(self):
        courses = self.course_set.filter(is_classics=True)[:3]
        return courses

    class Meta:
        verbose_name = "課程機構"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name