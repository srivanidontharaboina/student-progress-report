from django.shortcuts import render

from result.models import Student


def home(request):
    students=Student.objects.all()
    context={
        'students' :students,
    }
    return render(request,'home.html',context)