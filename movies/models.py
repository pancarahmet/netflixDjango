from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Kategori(models.Model):
    name=models.CharField(max_length=50,verbose_name="Kategori adı")
    def __str__(self):
        return self.name

class Tur(models.Model):
    name=models.TextField(max_length=50)

    def __str__(self):
        return self.name

class Movies(models.Model):
    filmismi=models.CharField(max_length=100,verbose_name='Film Adı')
    tur=models.ManyToManyField('Tur',null=True)
    aciklama=models.TextField(max_length=600,verbose_name='Film Açıklaması')
    resim=models.FileField(upload_to='afis',blank=True,null=True,verbose_name="Afiş")
    katagori=models.ForeignKey(Kategori,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.filmismi
    
class Izlenenler(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    izlenen=models.ManyToManyField('Movies',null=True)

    def __str__(self):
        return self.user.username
