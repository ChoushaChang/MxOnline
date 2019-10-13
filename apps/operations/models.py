from django.db import models

from django.contrib.auth import get_user_model

from apps.users.models import BaseModel
from apps.courses.models import Course

UserProfile = get_user_model()


class Banner(BaseModel):
    title = models.CharField(max_length=100, verbose_name="標題")
    image = models.ImageField(upload_to="banner/%Y/%m", max_length=200, verbose_name="輪播圖")
    url = models.URLField(max_length=200, verbose_name="訪問地址")
    index = models.IntegerField(default=0, verbose_name="順序")

    class Meta:
        verbose_name = "輪播圖"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class UserAsk(BaseModel):
    name = models.CharField(max_length=20, verbose_name="姓名")
    mobile = models.CharField(max_length=11, verbose_name="手機號")
    course_name = models.CharField(max_length=50, verbose_name="課程名")

    class Meta:
        verbose_name = "用戶咨詢"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{name}_{course}({mobile})".format(name=self.name, course=self.course_name, mobile=self.mobile)


class CourseComments(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用戶")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="課程")
    comments = models.CharField(max_length=200, verbose_name="評論内容")

    class Meta:
        verbose_name = "課程評論"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comments


class UserFavorite(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用戶")
    fav_id = models.IntegerField(verbose_name="數據id")
    fav_type = models.IntegerField(choices=((1,"課程"),(2,"課程機構"),(3,"講師")), default=1, verbose_name="收藏類型")

    class Meta:
        verbose_name = "用戶收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{user}_{id}".format(user=self.user.username, id=self.fav_id)


class UserMessage(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    message = models.CharField(max_length=200, verbose_name="消息内容")
    has_read = models.BooleanField(default=False, verbose_name="是否已讀")

    class Meta:
        verbose_name = "用戶消息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message


class UserCourse(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用戶")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="課程")

    class Meta:
        verbose_name = "用戶課程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course.name