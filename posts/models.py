from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    profile=models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title=models.CharField(max_length=255,blank=True,null=True)
    content_text=models.TextField(blank=False, null=False)
    photo=models.ImageField(upload_to='posts/pictures', null=True, blank=True)
    
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f'{self.title} by @{self.user.username}')
    