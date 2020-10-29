from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    description=models.TextField(blank=True)
    birthday=models.IntegerField(blank=True,unique_for_date=True,default="0")
    birthmonth=models.IntegerField(blank=True,unique_for_month=True,default="0")
    birthyear=models.IntegerField(blank=True,unique_for_year=True,default="0")

    phone_number=models.CharField(
        max_length=20,
        blank=True
    )
    picture=models.ImageField(
        upload_to='users/pictures',
        null=True
    )

    created= models.DateTimeField(auto_now_add=True)

    modified= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username