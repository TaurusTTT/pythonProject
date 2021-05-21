from django.db import models

# Create your models here.
class stuInfo(models.Model):
	objects = None
	stu_id = models.CharField(primary_key=True,max_length=13)
	stu_name = models.CharField(max_length=20)
	stu_vacci = models.CharField(max_length=5)