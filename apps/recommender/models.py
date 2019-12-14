from django.db import models

# Create your models here.
class Recs(models.Model):
    user = models.CharField(max_length = 16)
    item = models.CharField(max_length = 16)
    rating = models.FloatField()
    type = models.CharField(max_length = 16)

    class Meta:
        db_table = 'recs'

    def __str__(self):
        return "(u,i, t)({}, {}, {})= {}".format(self.user,
                                                 self.item,
                                                 self.type,
                                                 self.rating)