from django.shortcuts import render, HttpResponse, redirect
from authentication.models import User
from property.models import Property
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')


def new(request):
    if 'id' in request.session:
        user = User.objects.get(id=request.session['id'])
        if user.user_type=='landlord':
            return render(request,'form.html')
        return  redirect('/dashboard')

def edit(request):
    if 'id' in request.GET:
        prop=Property.objects.get(id=request.GET["id"])
        return render(request,'edit_form.html',{'prop':prop})
    return  redirect('/dashboard')

def create(request):
    if 'id' in request.session:
        user = User.objects.get(id=request.session['id'])
        errors = Property.objects.validator(request.POST)
        if len(errors):
            for tag, error in errors.items():
                messages.error(request, tag+" "+error, extra_tags=tag)
            return redirect('/properties/new')
        prop = Property.objects.create(owner=user, title=request.POST['title'], address=request.POST['address'], description=request.POST['description'], bond_amt= request.POST['bond_amt'], rent=request.POST['rent'], available_from=request.POST['available_from'], approved=2, reason="", property_pics=request.FILES['property_pics'])
        messages.success(request, "Property created ")
    return  redirect('/dashboard')

def update(request):
    if 'id' in request.GET:
        prop=Property.objects.get(id=request.GET["id"])
        prop.__class__.objects.update( title=request.POST['title'], address=request.POST['address'], description=request.POST['description'], bond_amt= request.POST['bond_amt'], rent=request.POST['rent'], available_from=request.POST['available_from'], approved=2, reason="")
        if len(request.FILES)>0:
            prop.property_pics=request.FILES['property_pics']
        prop.save()
        messages.success(request, "Property updated ")
    return  redirect('/dashboard')
    
def delete(request):
    id=request.GET["id"]
    Property.objects.get(id=id).delete()
    messages.success(request, "Property deleted")
    return redirect('/dashboard')

def change_list_status(request):
    prop=Property.objects.get(id=request.GET["id"])
    prop.listed=not prop.listed
    prop.save()
    return redirect('/dashboard')

def view(request):
    prop=Property.objects.get(id=request.GET["id"])
    # import pdb; pdb.set_trace()
    return render(request, 'show.html',{'comments': prop.comment_set.all(),'prop':prop,'current_user':User.objects.get(id=request.session['id'])})