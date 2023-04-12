from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=500)
    yili = models.CharField(max_length=100)
    davlat = models.CharField(max_length=500)
    davomiyligi = models.CharField(max_length=500)
    vidio = models.CharField(max_length=500)
    discription = models.TextField(blank=True,null=True)
    rasm = models.CharField(max_length=500)

    def __str__(self):
        return self.title