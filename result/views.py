from django.shortcuts import get_object_or_404, render

from result.models import Student


def student_detail(request,pk):
    student=get_object_or_404(Student,pk=pk)
    context={
        'student':student,

    }
    