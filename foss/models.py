from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=300)

class foss(models.Model):
    name=models.CharField(max_length=1000)

class tutorial_detail(models.Model):
    foss=models.ForeignKey(foss,on_delete=models.CASCADE)
    tutorial_name=models.CharField(max_length=1000)
    exp_sub_date=models.DateField()
    act_sub_date=models.DateField()
    publisher=models.ForeignKey(user,on_delete=models.CASCADE)
    
class payment(models.Model):
    publisher=models.ForeignKey(user,on_delete=models.CASCADE)
    payment=models.IntegerField()

