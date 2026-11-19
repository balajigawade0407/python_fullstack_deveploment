from django.shortcuts import render
from django.http import HttpResponse
from .models import Student_table
# Create your views here.
def home(request):
    data = {
        'name': 'John Doe',
        'age': 20,
        'department': 'Computer Science'
    }
    return render(request, 'home.html', data)

def contact(request):
    data = {
        'contact_number': '+91 1234567890',
        'address': 'Hubballi karnataka india',
        'contact_name': 'Balaji'
    }
    return render(request, 'contact.html', data)

def about(request):
    data = {
        'about_text': 'KLE SOCIETYS BCA PC JABIN CLG OF ARTS, COMMERCE AND SCIENCE, BELAGAVI'
    }
    return render(request, 'about.html', data)
def add(request):
    if request.method == 'POST':
        reg_no = request.POST.get('reg_no')
        name = request.POST.get('name')
        email = request.POST.get('email')
        marks = request.POST.get('marks')
        date = request.POST.get('date')

        # Create a new Student_table object and save it to the database
        student = Student_table(reg_no=reg_no, name=name, email=email, marks=marks, date=date)
        student.save()

        return HttpResponse("Student added successfully!")
    else:
        return render(request, 'studentform.html')