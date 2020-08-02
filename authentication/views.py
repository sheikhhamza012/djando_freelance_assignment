from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User



#SHOW SIGN UP PAGE
def new(request):
    return render(request,'signup.html')

#SHOW LOGIN PAGE
def login(request):
    if 'id' in request.session:
        return  redirect('/dashboard')
    return render(request,'login.html')

#SHOW CREATE USER RECIEVED FROM SIGNUP
def create(request):
    errors = User.objects.validator(request.POST)
    #MAP ERRORS
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/register')
    user = User.objects.create(user_type=request.POST['user_type'], name=request.POST['name'], password=request.POST['password'], email=request.POST['email'])
    user.save()
    request.session['id'] = user.id
    messages.success(request, "Registeration complete , you can login now ")
    return redirect('/')

#SHOW MAKE LOGIN FROM LOGIN PAGE
def create_session(request):
    #VALIDATION
    if (len(request.POST['email'])>0 or len(request.POST['password'])>0):
        if (User.objects.filter(email=request.POST['email']).exists()):
            user = User.objects.filter(email=request.POST['email'])[0]
            #CONFIRM PASSWORD
            if (request.POST['password']== user.password):
                request.session['id'] = user.id
                return redirect('/dashboard')   
            messages.error(request, "email/password mismatch")
            return redirect('/')
        messages.error(request, "User doesnot exist")
        return redirect('/')
    messages.error(request, "please fill the form")
    return redirect('/')

#LOGOUT USER
def logout(request):
    del request.session['id']
    return redirect('/')
