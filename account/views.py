from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('account:login_view')
        else:
            msg = 'form is not valid'
    
    else:
        form = SignUpForm()
    context = {'form': form, 'msg': msg}
    return render(request, 'account/register.html', context)


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            #username = form.cleaned_data.get('username')
            #password = form.cleaned_data.get('password')
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_pmd:
                login(request, user)
                return redirect('job_order:index')
            elif user is not None and user.is_uto:
                login(request, user)
                return redirect('job_order:index')
            elif user is not None and user.is_qa:
                login(request, user)
                return redirect('job_order:index')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    context = {'form': form, 'msg': msg}
    return render(request, 'account/login.html', context)    

def logout_view(request):
    logout(request)
    msg = 'Thank you, have a nice day!!!'
    context = {'msg': msg}
    return render(request, 'account/logout.html', context)
