from django.contrib import admin

from .models import Lesson, Course, Teacher, Student


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = "id", "theme", "course"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = "id", "name"


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass
