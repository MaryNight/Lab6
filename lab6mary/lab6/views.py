from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from django.views.generic import TemplateView

from lab6.models import Lesson

# Create your views here.

class ExampleView(View):
    def get(self, request):
        return render(request, 'base.html')

class LessonsView(ListView):
    model = Lesson
    context_object_name = 'lessons'
    template_name = 'lessons.html'
    
    def get_queryset(self):
        qs = Lesson.objects.all().order_by('id')
        return qs

class LessonView(View):
    def get(self, request, id):
        data = Lesson.objects.get(id__exact=id)
        return render(request, 'lesson.html', {'lesson':data})
