from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Course, Lesson, Teacher


def course_list(request: HttpRequest):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, "app/courses.html", context)


def lesson_list(request: HttpRequest, id=None):
    if id:
        lessons = Lesson.objects.filter(course_id=id)
    else:
        lessons = Lesson.objects.all()
    context = {
        'lessons': lessons
    }
    return render(request, "app/lessons.html", context)


def teacher_list(request: HttpRequest):
    context = {
        'teachers': Teacher.objects.all()
    }
    return render(request, "app/teachers.html", context)