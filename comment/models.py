from django.db import models
from authentication.models import User
from property.models import Property
# Create your models here.
class CommentManager(models.Manager):
    def validator(self, postData):
        errors = {}
        for name, val in postData.items():
            if(len(val)==0):
                errors[name]="please fill the field"
        return errors
class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    body = models.CharField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=CommentManager()