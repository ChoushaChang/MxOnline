from django.db import models

# Create your models here.
class Log(models.Model):
    created = models.DateTimeField('date happened')
    user_id = models.CharField(max_length = 16)
    Course_or_Org_id = models.CharField(max_length = 16)
    event = models.CharField(max_length = 200)
    session_id = models.CharField(max_length = 128)

    def __str__(self):
        return "user_id: {}, course_id: {},event: {}".format(self.user_id,
                                                              str(self.course_id),
                                                              self.event)
