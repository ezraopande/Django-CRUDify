from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Student

import os


# Create your views here.

# here is where all functions are created


def Home(request):
    return render(request, 'home.html', {'navbar': 'home'})


def about(request):
    return render(request, 'about.html', {'navbar': 'about'})


def contact(request):
    return render(request, 'pages/contact.html', {'navbar': 'contact'})


def add(request):
    return render(request, 'add.html', {'navbar': 'add'})


def viewdata(request):
    students = Student.objects.all()
    return render(request, 'viewdata.html', {'navbar': 'viewdata', 'data': students})


def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("/viewdata")


def insertdata(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        image = request.FILES['image']

        room = Student(name=name, email=email, age=age, image=image)
        room.save()
        return redirect("/viewdata")

    return redirect("/viewdata")


def edit(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST['age']
        image = request.FILES['image']

        student = Student.objects.get(id=id)

        student.name = name
        student.email = email
        student.age = age
        student.image = image

        if len(request.FILES) != 0:
            if len(student.image) > 0:
                student.image = request.FILES['image']

        student.save()
        return redirect("/viewdata")

    student = Student.objects.get(id=id)
    return render(request, 'edit.html', {'student':student})


def details(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'details.html', {'student':student})
