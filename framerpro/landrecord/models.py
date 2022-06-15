from django.db import models

class LandRec(models.Model):
    farmer_name = models.CharField(max_length=50)
    survey_number = models.CharField(max_length=10)
    village = models.CharField(max_length=50)
    farm_area = models.CharField(max_length=20)
    framer_image = models.ImageField(upload_to='images/',default='images/default.jpg', blank=True, null=True)


    


# Create your models here.
