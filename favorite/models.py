from django.db import models
from authentication.models import User
from property.models import Property
# VALIDATION
class FavoriteManager(models.Manager):
    def validator(self, postData):
        errors = {}
        for name, val in postData.items():
            if(len(val)==0):
                errors[name]="please fill the field"
        return errors
#TABLE WITH USER AND POST REF
class Favorite(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
 
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=FavoriteManager()