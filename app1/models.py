from django.contrib.auth.models import User
from django.db import models


class Muallif(models.Model):
    ism=models.CharField(max_length=120)
    tugulgan_sana=models.DateField()
    maqolalar_soni=models.SmallIntegerField()
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.ism
class Maqola(models.Model):
    sarlavha=models.CharField(max_length=120)
    sana=models.DateField()
    mavzu=models.CharField(max_length=120,blank=True)
    matn=models.TextField()
    muallif=models.ForeignKey(Muallif,on_delete=models.CASCADE)
    def __str__(self):
        return self.sarlavha