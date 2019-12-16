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

class SeededRecs(models.Model):
    created = models.DateTimeField()
    source = models.CharField(max_length=16)
    target = models.CharField(max_length=16)
    support = models.DecimalField(max_digits=10, decimal_places=8)
    confidence = models.DecimalField(max_digits=10, decimal_places=8)
    type = models.CharField(max_length=8)

    class Meta:
        db_table = 'seeded_recs'

    def __str__(self):
        return "[({} => {}) s = {}, c= {}]".format(self.source,
                                                    self.target,
                                                    self.support,
                                                    self.confidence)