from django.db import models


class User(models.Model):
    email = models.CharField(max_length=255, blank=False, unique=True)
    username = models.CharField(max_length=255, blank=False)
    password = models.CharField(max_length=255, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.email
