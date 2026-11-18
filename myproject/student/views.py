from django.shortcuts import render
from django.http import HttpResponse

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