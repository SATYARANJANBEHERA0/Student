from django.shortcuts import render,redirect
from Testapp.models import Student
from Testapp.forms import StudentForm
from Testapp.forms import SignUpForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
# Retrive View
def retrive_view(request):
    student_list = Student.objects.all()
    return render(request,'Testapp/home.html',{'student_list':student_list})

# detailview
class StudentDetailView(DetailView):
    model = Student

# Create data
def insert_view(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/')
    return render(request,'Testapp/insert.html',{'form':form})

# update data
@login_required
def update_view(request,id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance = student)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'Testapp/update.html',{'form':form})

# Signup form
def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'Testapp/signup.html',{'form':form})

# Logout
def logout_view(request):
    return render(request,'Testapp/logout.html')
