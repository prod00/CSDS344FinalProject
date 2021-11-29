from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    case_id = models.CharField(max_length=10)
    gpa = models.CharField(max_length=3)

    class Meta:
        db_table = 'Student'


class ReportCard(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    midterm_grade = models.IntegerField()
    final_grade = models.IntegerField()

    class Meta:
        db_table = 'ReportCard'



