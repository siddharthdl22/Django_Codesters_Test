from django.shortcuts import render
from studentwebsite import services
from django.http import JsonResponse


def get_teacher_view(request):
    get_view = services.teacher_view()
    return JsonResponse(get_view, safe = False)

def show_teacher_page(request):
    return render(request, 'studentwebsite/index.html')
