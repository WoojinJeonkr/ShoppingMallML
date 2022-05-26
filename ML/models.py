from django.db import models

# Create your models here.
class Tag(models.Model):
    week1 = models.IntegerField(100)
    week2 = models.IntegerField(100)
    hour = models.IntegerField(100)
    gender = models.IntegerField(100)
    age = models.IntegerField(100)
    size = models.IntegerField(10000)
    tag_click = models.IntegerField(300)

    def __str__(self):
        return str(self.id) + ", " + str(self.week1) + ", " + \
               str(self.week2) + ", " + str(self.hour) + ", " + \
               str(self.gender) + ", " + str(self.age) + ", " + \
               str(self.size) + ", " + str(self.tag_click)