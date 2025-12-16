from django.db import models

# Create your models here.

class Kurtka(models.Model):
    nomi=models.CharField(max_length=200)
    brend=models.CharField(max_length=200)
    rang=models.CharField(max_length=200)
    narx=models.DecimalField(decimal_places=2,max_digits=10)
    skidka=models.IntegerField(default=0)

    def __str__(self):
        return self.nomi

class Futbolka(models.Model):
    nomi=models.CharField(max_length=200)
    davlat=models.CharField(max_length=200)
    brend=models.CharField(max_length=225)
    info=models.CharField(max_length=200)
    rang=models.CharField(max_length=200)
    narx=models.DecimalField(decimal_places=2,max_digits=10)
    sotuvdagi_soni=models.DecimalField(decimal_places=2,max_digits=10)

    def __str__(self):
        return self.brend


class Telefon(models.Model):
    class RamChoices(models.TextChoices):
        gb4 = "gb4" , "4 gb"
        gb8 = "gb8" , "8 gb"

    class ColorChoices(models.TextChoices):
        black = "qora" , "Qora"
        white = "oq" , "oq"
        red = "qizil" , "Qizil"

    class BrandChoices(models.TextChoices):
        samsung = "samsung" , "mol"
        Iphone = "iphone"  , "oypon"

    narx = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to="product/")
    color = models.CharField(max_length=30, choices=ColorChoices.choices)
    brend = models.CharField(max_length=30, choices=BrandChoices.choices)
    ram = models.CharField(max_length=30, choices=RamChoices.choices)

    def __str__(self):
        return self.brend