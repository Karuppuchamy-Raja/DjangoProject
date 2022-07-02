from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

# Create your views here.


def login(request):
    if(request.method=='POST'):
        uname = request.POST['uname']
        pass1 = request.POST['pass1']
        
        currentUser = auth.authenticate(username=uname, password=pass1)
        if(currentUser is not None):
            auth.login(request, currentUser)
            return redirect('/')
        else:
            msg={'err':f'The Username or Password is incorrect'}
            return render(request, 'usererr.html', msg)
    context={}
    return render(request, 'login.html', context)

def signup(request):
    if(request.method == 'POST'):
        uname = request.POST['uname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if(pass1==pass2):
            if(not(User.objects.filter(username=uname).exists())):
                newUser = User.objects.create_user(username=uname, password=pass1, email=email)
                newUser.save()
                return redirect('/accounts/login/')
            else:
                msg={'err':f'Sorry! The username {uname} is alredy taken, Please try someothing else'}
                return render(request, 'error.html', msg)
        else:
            msg={'err':'The Password Dosen\'t matches'}
            return render(request, 'error.html', msg)
    else:
        context={}
        return render(request, 'signup.html', context)

def logout(request):
    auth.logout(request)
    return redirect('/')