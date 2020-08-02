from django.shortcuts import render, HttpResponse, redirect
from authentication.models import User
from property.models import Property
from django.contrib import messages


def index(request):
    return render(request,'index.html')

# SHOW CREATE FORM
def new(request):
    if 'id' in request.session:
        user = User.objects.get(id=request.session['id'])
        if user.user_type=='landlord':
            return render(request,'form.html')
        return  redirect('/dashboard')

# SHOW EIDT FORM
def edit(request):
    if 'id' in request.GET:
        prop=Property.objects.get(id=request.GET["id"])
        return render(request,'edit_form.html',{'prop':prop})
    return  redirect('/dashboard')

# CREATE PROPERTY AND SAVE IN DB
def create(request):
    #CHECK USER LOGGED IN
    if 'id' in request.session:
        user = User.objects.get(id=request.session['id'])
        #CHECK ERRORS
        errors = Property.objects.validator(request.POST)
        if len(errors):
            for tag, error in errors.items():
                #SHOW ERROR
                messages.error(request, tag+" "+error, extra_tags=tag)
            return redirect('/properties/new')
        # CREATE PROPERTY
        prop = Property.objects.create(owner=user,rooms=request.POST['rooms'], title=request.POST['title'], address=request.POST['address'], description=request.POST['description'], bond_amt= request.POST['bond_amt'], rent=request.POST['rent'], available_from=request.POST['available_from'], approved=2, reason="", property_pics=request.FILES['property_pics'])
        messages.success(request, "Property created ")
    return  redirect('/dashboard')


#UPDATE PROPERTY
def update(request):
    #CHECK LOGIN
    if 'id' in request.GET:
        prop=Property.objects.get(id=request.GET["id"])
        prop.__dict__.update( title=request.POST['title'],rooms=request.POST['rooms'],address=request.POST['address'], description=request.POST['description'], bond_amt= request.POST['bond_amt'], rent=request.POST['rent'], available_from=request.POST['available_from'], approved=2, reason="")
        #IF CAME NO IMAGE, DONT UPDATE
        if len(request.FILES)>0:
            prop.property_pics=request.FILES['property_pics']
        prop.save()
        messages.success(request, "Property updated ")
    return  redirect('/dashboard')

#FIND AND DELETE THE POST
def delete(request):
    id=request.GET["id"]
    Property.objects.get(id=id).delete()
    messages.success(request, "Property deleted")
    return redirect('/dashboard')

#IF PROPERTY IS LISTED UNLIST IT
def change_list_status(request):
    prop=Property.objects.get(id=request.GET["id"])
    #CHANGE STATUS
    prop.listed=not prop.listed
    prop.save()
    return redirect('/dashboard')

#APPROVE THE POST BY REVIEWER
def approve(request):
    prop=Property.objects.get(id=request.GET["id"])
    prop.approved=1
    prop.reason=request.POST['reason']
    prop.save()
    return redirect('/dashboard')

#DISAPPROVE THE POST BY REVIEWER
def disapprove(request):
    prop=Property.objects.get(id=request.GET["id"])
    prop.approved=0
    prop.reason=request.POST['reason']
    prop.save()
    return redirect('/dashboard')

#VIEW THE PROPERTY
def view(request):
    prop=Property.objects.get(id=request.GET["id"])
    return render(request, 'show.html',{'comments': prop.comment_set.all(),'prop':prop,'reviewer':User.objects.get(id=request.session['id']).user_type=="reviewer"})