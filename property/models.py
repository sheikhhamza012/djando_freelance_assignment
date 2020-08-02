from django.db import models
from authentication.models import User
# VALIDATION
class PostManager(models.Manager):
    def validator(self, postData):
        errors = {}
        for name, val in postData.items():
            if(len(val)==0):
                errors[name]="please fill the field"
        return errors
#DEFINITION
class Property(models.Model):
    title = models.CharField(max_length=10000)
    address = models.CharField(max_length=10000)
    description = models.CharField(max_length=10000)
    bond_amt = models.IntegerField(default=0)
    rent = models.IntegerField(default=0)
    listed = models.BooleanField(default=True)
    available_from = models.DateField(auto_now = True)
    approved = models.IntegerField(default=2)
    rooms = models.IntegerField(default=0)
    reason=models.CharField(max_length=10000)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    property_pics = models.ImageField(upload_to='images/') 
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=PostManager()