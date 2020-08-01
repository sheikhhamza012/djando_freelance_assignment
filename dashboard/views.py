from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from authentication.models import User
from property.models import Property

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
def student(request):
    return render(request,'student.html')
def reviewer(request):
    return render(request,'reviewer.html')
def landlord(request):
    user = User.objects.get(id=request.session["id"])
    approved=user.property_set.filter(approved=1,listed=True)
    rejected=user.property_set.filter(approved=0,listed=True)
    pending=user.property_set.filter(approved=2,listed=True)
    unlisted=user.property_set.filter(listed=False)
    # import pdb; pdb.set_trace()

    return render(request,'landlord.html',{
        'approved':approved,
        'rejected':rejected,
        'pending':pending,
        'unlisted':unlisted,

    })