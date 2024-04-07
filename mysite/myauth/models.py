from django.contrib.auth.models import User
from django.db import models
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Bio = models.TextField(max_length=600,blank = True)
    agreement_accepted = models.BooleanField(default = False)
# Create your models here.
