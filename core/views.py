from django.shortcuts import get_object_or_404, redirect, render
from .models import Student
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

def home(request):
    student = Student.objects.all()
    return render(request, "index.html", {"students": student})


def save(request):
    name = request.POST.get("name")
    age = request.POST.get("age")
    first_semester_grade = request.POST.get("first_semester_grade")
    second_semester_grade = request.POST.get("second_semester_grade")
    professor_name = request.POST.get("professor_name")
    classroom_number = request.POST.get("classroom_number")
    
    Student.objects.create(
        name=name,
        age=age,
        first_semester_grade=first_semester_grade,
        second_semester_grade=second_semester_grade,
        professor_name=professor_name,
        classroom_number=classroom_number
    )
    
    student = Student.objects.all()
    return render(request, "index.html", {"students": student})

def edit(request, id):
    student = Student.objects.get(id=id)
    return render(request, "update.html", {"student": student})
    
def update(request, id):
    name = request.POST.get("name")
    age = request.POST.get("age")
    first_semester_grade = request.POST.get("first_semester_grade")
    second_semester_grade = request.POST.get("second_semester_grade")
    professor_name = request.POST.get("professor_name")
    classroom_number = request.POST.get("classroom_number")  
    
    student = Student.objects.get(id=id)
    
    student.name = name
    student.age = age
    student.first_semester_grade = first_semester_grade
    student.second_semester_grade = second_semester_grade
    student.professor_name = professor_name
    student.classroom_number = classroom_number
    
    student.save()
    return redirect(home)

def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect(home)
