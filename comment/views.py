from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from authentication.models import User
from property.models import Property
from comment.models import Comment

#CREATE A COMMENT TO THE POST
def create(request):
    user = User.objects.get(id=request.session['id'])
    prop = Property.objects.get(id=request.POST['prop_id'])
    comment = Comment.objects.create(body=request.POST['body'],owner=user,property=prop)
    return redirect('/properties/view?id='+str(prop.id))
