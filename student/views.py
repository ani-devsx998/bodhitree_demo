from django.shortcuts import render
from django.http import JsonResponse
from .models import Student

# Homepage
def home(request):
    return render(request, 'index.html')


# API endpoint
def get_students(request):

    students = Student.objects.all().order_by('-marks')

    highest_marks = students.first().marks if students.exists() else 0

    data = []

    rank = 1

    for s in students:
        data.append({
            "roll_no": s.roll_no,
            "name": s.name,
            "marks": s.marks,
            "highest_marks": highest_marks,
            "time_taken": s.time_taken,
            "rank": rank
        })

        rank += 1

    return JsonResponse(data, safe=False)