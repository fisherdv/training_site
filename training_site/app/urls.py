from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='courses'),
    path('lessons/<int:id>', views.lesson_list, name='lessons'),
    path('lessons', views.lesson_list, name='all_lessons'),
    path('teachers', views.teacher_list, name='teachers'),

]
