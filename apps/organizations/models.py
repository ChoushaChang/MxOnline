from django.db import models
from DjangoUeditor.models import UEditorField

from apps.users.models import BaseModel


class City(BaseModel):
    name = models.CharField(max_length=20, verbose_name=u"城市名")
    desc = models.CharField(max_length=200, verbose_name=u"描述")

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(BaseModel):
    name = models.CharField(max_length=50, verbose_name="機構名稱")
    desc = UEditorField(verbose_name="描述", width=600, height=300, imagePath="courses/ueditor/images/",
                          filePath="courses/ueditor/files/", default="")
    tag = models.CharField(default="全國知名", max_length=10, verbose_name="機構標簽")
    category = models.CharField(default="pxjg", verbose_name="機構類別", max_length=4,
                                choices=(("pxjg", "培訓機構"), ("gr", "個人"), ("gx", "高校")))
    click_nums = models.IntegerField(default=0, verbose_name="點擊數")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏數")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="logo", max_length=100)
    address = models.CharField(max_length=150, verbose_name="機構地址")
    students = models.IntegerField(default=0, verbose_name="學習人數")
    course_nums = models.IntegerField(default=0, verbose_name="課程數")

    is_auth = models.BooleanField(default=False, verbose_name="是否認證")
    is_gold = models.BooleanField(default=False, verbose_name="是否金牌")

    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="所在城市")

    def courses(self):
        courses = self.course_set.filter(is_classics=True)[:3]
        return courses

    class Meta:
        verbose_name = "課程機構"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

from apps.users.models import UserProfile
class Teacher(BaseModel):
    user = models.OneToOneField(UserProfile, on_delete=models.SET_NULL, null=True, blank=True,verbose_name="用戶")
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="所屬機構")
    name = models.CharField(max_length=50, verbose_name=u"教師名")
    work_years = models.IntegerField(default=0, verbose_name="工作年限")
    work_company = models.CharField(max_length=50, verbose_name="就職公司")
    work_position = models.CharField(max_length=50, verbose_name="公司職位")
    points = models.CharField(max_length=50, verbose_name="教學特點")
    click_nums = models.IntegerField(default=0, verbose_name="點擊數")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏數")
    age = models.IntegerField(default=18, verbose_name="年齡")
    image = models.ImageField(upload_to="teacher/%Y/%m", verbose_name="頭像", max_length=100)

    class Meta:
        verbose_name = "教師"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def course_nums(self):
        return self.course_set.all().count()
