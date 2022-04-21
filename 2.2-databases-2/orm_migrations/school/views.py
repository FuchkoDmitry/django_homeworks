from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    # object_list = Student.objects.order_by('group') # 4queries 35ms
    object_list = Student.objects.order_by('group').prefetch_related('teachers')  # 2 queries 28ms
    context = {'object_list': object_list}
    return render(request, template, context)
