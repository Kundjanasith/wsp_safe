#utf-8
from django.db import models

# Create your models here.
class User (models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20, default='no')
    อาจารย์อยาได้อะไรค้าบ = models.CharField(max_length=20 , default='ไม่บอก')
    ที่อยู่ = models.CharField(max_length=20, default='ไม่บอกนะอิอิ')