from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Student, StudyGroup


def index(request):
    return HttpResponse("Глaвнaя страница базы данных студентов" )


# def detail(request, student_id):
#     try:
#         s = Student.objects.get(id=student_id)
#     except Exception:
#         raise Http404("Данные не найдены")
#
#     return render(request, "students1/detail.html", {'student_id': s.student_id,
#                                                      'last_name': s.last_name,
#                                                      'first_name': s.first_name,
#                                                      'patronymic_name': s.patronymic_name,
#                                                      'date_of_birth': s.date_of_birth,
#                                                      'study_group': s.study_group})
