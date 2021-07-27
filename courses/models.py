from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from teachers.models import Teacher
from students.models import Student


STATUS = (
    ('Passed', 'Passed'),
    ('Failed', 'Failed'),
    ('Pending', 'Pending'),
)


class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    credit = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Instructor(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    about = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('course', 'teacher')

    def __str__(self):
        return f'{self.course.title} - {self.teacher.__str__()}'


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(
        blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(100)])
    grade = models.CharField(max_length=5, blank=True, null=True)
    status = models.CharField(choices=STATUS, max_length=10, default='Pending')
    comments = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('course', 'student')

    def __str__(self):
        return f'{self.student.__str__()} takes {self.course.course.title}'
