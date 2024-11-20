from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
  def __str__(self):
    return self.user.username

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  avatar = models.ImageField(default='profilepic.jpg', upload_to='avatar_pictures')
  follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)
  