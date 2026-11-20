from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Student_table
from .forms import Studentform_data


def home(request):
    data1 = {
        'name': "Balaji",
        'age': 19,
        'department': "BCA"
    }
    marks = [100, 99, 98]

    return render(request, 'home.html', {
        **data1,
        'marks1': marks
    })


def about(request):
    return render(request, 'about.html')


def contact(request):
    # Replace these placeholder values with your real details
    return render(request, 'contact.html', {
        'contact_name': "College Office",
        'contact_number': "0000000000",
        'address': "Add your college address here",
    })


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
                return render(request, 'studentformdata.html', {'form': form})

            Student_table.objects.create(
                reg_no=reg_no,
                name=form.cleaned_data['name1'],
                email=form.cleaned_data['email1'],
                marks=form.cleaned_data['marks1'],
                date=form.cleaned_data['dob1'],
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

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        messages.error(request, 'Invalid username or password.')
        return render(request, 'login.html')

    return render(request, 'login.html')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')


def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'logged_out.html')

    return redirect('login')