from django.shortcuts import render, redirect
from .models import ReportCard, Student
from django.db.models import Q
from django.contrib import messages

def home(request):

    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(Q(name__icontains=query)| Q(case_id__icontains=query))

        context = {
            'students': students
        }
    else:
        all_students = Student.objects.all()

        context = {
         'students': all_students,
        }

    return render(request, 'main_site/base.html', context)

def teacher_login(request):
    return render(request, 'main_site/login.html')

def login_redirect(request):
    password = request.POST.get('password')
    if password == "password":
        return redirect('teacher_home')
    else:
        messages.error(request, 'Incorrect Password!')
        return redirect('teacher_login')

def teacher_home(request):
    query = request.GET.get('q')
    if query:
        reportcards = ReportCard.objects.filter(Q(student__name__icontains=query) | Q(student__case_id__icontains=query))
        print(reportcards)
        context = {
            'reportcards': reportcards
        }
    else:
        reportcards = ReportCard.objects.all()
        print(reportcards)

        context = {
            'reportcards': reportcards,
        }

    return render(request, 'main_site/teacher_home.html', context)
