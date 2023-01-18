from django.db import models


class UserModel(models.Model):
    email = models.CharField(max_length=255, blank=False)
    username = models.CharField(max_length=255, blank=False)
    password = models.CharField(max_length=255, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
