from django.db import models

# Create your models here.

class MandirModel(models.Model):
    mandir_id=models.AutoField(primary_key=True)
    mandir_name=models.CharField(max_length=50)
    mandir_address=models.CharField(max_length=500)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    description = models.TextField()
    mandir_date = models.DateField()
    timings = models.CharField(max_length=100)
    mandir_isfor = models.CharField(max_length=100)
    history = models.TextField()
    rating = models.FloatField()
    

    