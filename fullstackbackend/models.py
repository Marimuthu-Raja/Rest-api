from django.db import models


class UserDetails(models.Model):

    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


    def __string__(self):
        return self.UserDetails