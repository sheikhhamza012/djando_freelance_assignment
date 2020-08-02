from django.shortcuts import render, HttpResponse, redirect
from authentication.models import User
from property.models import Property
from favorite.models import Favorite
from django.contrib import messages

# CREATE A FAVORITE POST
def make(request):
    #FIND LOGGED IN USER
    user = User.objects.get(id=request.session['id'])
    prop = Property.objects.get(id=request.GET['id'])
    #CHECK IF ALREADY FAVORITE
    r=Favorite.objects.filter(owner=user,property=prop)
    #FAVORITE ONLY IF NOT ALREADY FAVORITE
    if len(r)==0:
        Favorite.objects.create(owner=user,property=prop)
        messages.success(request,"added to your favorites, goto favorites to see")
    return redirect('/dashboard')

# REMOVE FROM FAVORITE
def remove(request):
    #GET USER AND PROPERTY
    user = User.objects.get(id=request.session['id'])
    prop = Property.objects.get(id=request.GET['id'])
    #FIND AND REMOVE FROM FAVORITE
    r=Favorite.objects.get(owner=user,property=prop)
    r.delete()
    messages.success(request,"removed from your favorites")

    return redirect('/dashboard')


