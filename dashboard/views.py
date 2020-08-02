from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from authentication.models import User
from property.models import Property
from favorite.models import Favorite
# '/' WILL DECIDE WHICH USER IS LOGGED IN AND WILL SEND THEM TO THE PAGE THE SHOULD
def index(request):
    if 'id' in request.session:
        user = User.objects.get(id=request.session['id'])
        if(user.user_type=="landlord"):
            return redirect('/dashboard/landlord')
        if(user.user_type=="student"):
            return redirect('/dashboard/student')
        if(user.user_type=="reviewer"):
            return redirect('/dashboard/reviewer')
    return redirect('/')


#IF A STUDENT LOGS IN THIS HANDLES THE DASHBOARD
def student(request):
    #IF NOT A FILTER REQUEST THIS GETS THE POSTS
    props = Property.objects.filter(listed=True,approved=1)
    # RANGE FOR MIN TO MAX NO OF ROOMS
    ran = range(props.order_by('rooms').first().rooms,props.order_by('rooms').last().rooms)
    #MAX TO MIN PRICE RANGE 
    ran_p =range(props.order_by('rent').last().rent,props.order_by('rent').first().rent,-10)
    #IF A FILTER REQUES COMES GET FILTERED POSTS
    if len(request.POST)>0:
        #DEFAULT
        order="created_at"
        if request.POST['order']=='1':
            order="available_from"
        if request.POST['order']=='2':
            order="rent"
        #GET MIN AND MAX RENT SELECTED
        r= str(request.POST['rent']).split(' - ')
        #FILTER AND SAVE IN PROPS
        props = Property.objects.filter(listed=True,approved=1,rooms__gte= request.POST['rooms'],rent__lte=r[1],rent__gte=r[0]).order_by(order)
    #TO CHECK WHICH PROPS ARE ALREADY FAVORITE AND CREATE AN EQUAL SIZE ARRAY WITH TRUE VAL IF ALREADY FAV
    fav=[]
    for p in props:
        f= Favorite.objects.filter(owner=User.objects.get(id=request.session["id"]),property=p)
        if len(f)>0:
            fav.append(True)
        else:
            fav.append(False)
    return render(request,'student.html',{'props':zip(props,fav),'user':User.objects.get(id=request.session["id"]),'range': ran,'rangeprice': ran_p})

#SHOW FAVORITES PAGE
def favorites(request):
    favs = Favorite.objects.filter(owner=User.objects.get(id=request.session["id"]))
    props=[]
    #FROM FAVROITE TABLE GET PROPERTIES AND APPEND AND THEN SEND TO TEMPLATE
    for f in favs:
        props.append(f.property)
    return render(request,'favorites.html',{'props':props})

#DASHBOARD FOR REVIEWER, SHOWS PENDING POSTS
def reviewer(request):
    user = User.objects.get(id=request.session["id"])
    pending = Property.objects.filter(listed=True,approved=2)
    return render(request,'reviewer.html',{'pending':pending,'landlord':user.user_type=="landlord"})

#DASHBOARD FOR LANDLORD
def landlord(request):
    user = User.objects.get(id=request.session["id"])
    approved=user.property_set.filter(approved=1,listed=True)
    rejected=user.property_set.filter(approved=0,listed=True)
    pending=user.property_set.filter(approved=2,listed=True)
    unlisted=user.property_set.filter(listed=False)

    return render(request,'landlord.html',{
        'approved':approved,
        'rejected':rejected,
        'pending':pending,
        'unlisted':unlisted,

    })