from django.db import models
from django.contrib.auth import get_user_model


class Student(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.PROTECT, null=False)

    def __str__(self):
        return f"{self.user}"


class Teacher(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.PROTECT, null=False)
    describe = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user)


class Course(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    students = models.ManyToManyField(Student, blank=True)
    offline = models.BooleanField(default=False)
    start_date = models.DateField()

    def __str__(self):
        return str(self.name)


class Lesson(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    theme = models.CharField(max_length=128, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    event_date = models.DateField()
    event_time = models.TimeField()

    def __str__(self):
        return str(self.theme)
