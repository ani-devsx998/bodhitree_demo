from django.shortcuts import render
from django.http import JsonResponse
from .models import Student

def get_students(request):

    students = Student.objects.all()

    data = []

    for s in students:
        data.append({
            "roll_no": s.roll_no,
            "name": s.name,
            "marks": s.marks,
            "time_taken": s.time_taken
        })

    return JsonResponse(data, safe=False)