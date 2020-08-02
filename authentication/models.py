from __future__ import unicode_literals
from django.db import models

#VALIDATION
class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if (postData['name'].isalpha()) == False:
            if len(postData['name']) < 2:
                errors['name'] = "name can not be shorter than 2 characters"
        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"

        if len(postData['password']) < 4:
            errors['password'] = "Password is too short!"
        
        if postData['password'] != postData['cpassword']:
            errors['confirm_password'] = "Password does not match!"
        return errors
#MODEL
class User(models.Model):
    user_type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()