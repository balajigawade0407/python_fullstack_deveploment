from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student_table
from .forms import Studentform_data
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    data1 = {
        'name': "Abhishek",
        'age': 19,
        'department': "BCA"
    }

    marks = [100, 99, 98]

    return render(request, 'home.html', {
        'data1': data1,
        'marks1': marks
    })


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def forms1(request):
    if request.method == "POST":
        reg_no = request.POST.get('reg_no')
        name = request.POST.get('name')
        marks = request.POST.get('marks')
        email = request.POST.get('email')

        Student_table.objects.create(
            reg_no=reg_no,
            name=name,
            email=email,
            marks=marks
        )

        return HttpResponse("Saved successfully!!")

    return render(request, 'studentform.html')


def student_form_dj(request):
    if request.method == 'POST':
        form = Studentform_data(request.POST)

        if form.is_valid():
            reg_no = form.cleaned_data['reg_no1']

            if Student_table.objects.filter(reg_no=reg_no).exists():
                form.add_error(
                    'reg_no1',
                    'A student with this registration number is already registered.'
                )
                return render(
                    request,
                    'studentformdata.html',
                    {'form': form}
                )

            Student_table.objects.create(
                reg_no=reg_no,
                name=form.cleaned_data['name1'],
                email=form.cleaned_data['email1']
            )

            messages.success(request, 'Student registered successfully.')
            return redirect('student_form')

        return render(request, 'studentformdata.html', {'form': form})

    form = Studentform_data()
    return render(request, 'studentformdata.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("Invalid credentials. Please try again.")

    return render(request, 'login.html')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')


def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    return HttpResponse("Invalid request method. Please use POST to log out.")