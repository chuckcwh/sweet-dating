from django.contrib.auth.models import User
from django.db import models


class Portfolio(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    gender = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField(null=True)
    user_photo = models.ImageField(upload_to="user_photos", null=True, blank=True)
    user_photo2 = models.ImageField(upload_to="user_photos", null=True, blank=True)
    target_gender = models.CharField(max_length=20)

    def __unicode__(self):
        return u"{}".format(self.user)
