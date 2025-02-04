from django.db import models

# Create your models here.
class Tour(models.Model):
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.FloatField()

    def __str__(self) -> str:
        return super().__str__()
    
class FormInput(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=500)

    def __str__(self) -> str:
        return super().__str__()