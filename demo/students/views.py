from django.http import HttpResponse
from students.models import Student
from django.shortcuts import render

def home(request):
  name = request.GET.get("user_name", "Stranger")
  return render(request, 'base.html', {'name': name})

def students(request):
  students = Student.objects.all()
  return render(request, 'students.html', {'students': students})

def student(request, student_id):
  student = Student.objects.get(id=student_id)
  return render(request, 'student.html', {'student': student})
