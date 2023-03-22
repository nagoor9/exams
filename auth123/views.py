from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from auth123.forms import SignUpForm

# Create your views here.
def home_page_view(request):
    return render(request,'auth123/home.html')
def login_view(request):
    return render(request,'auth123/login/registration/login.html')

@login_required
def java_exams_view(request):
    return render(request, 'auth123/javaexams.html')
@login_required
def python_exams_view(request):
    return render(request, 'auth123/pythonexams.html')
@login_required
def aptitude_exams_view(request):
    return render(request, 'auth123/aptitudeexams.html')
def logout_view(request):
    return render(request,'auth123/logout.html')
def signup_view(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.post)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('login.html')
    return render(request,'signup.html',{'form':form})


