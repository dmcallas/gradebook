from django.db import models
from django.core.urlresolvers import reverse
from django.shortcuts import resolve_url

class Department(models.Model):
        name=models.CharField(max_length=10,primary_key=True,unique=True,blank=False)
        long_name=models.CharField(max_length=50,null=True,blank=True)
        def __str__(self):
                return self.long_name
                
class EnrollmentStatus(models.Model):
        description=models.CharField(max_length=20,unique=True,blank=False)
        def __str__(self):
                return self.description

class AssignmentType(models.Model):
        description=models.TextField(unique=True,blank=False)
        def __str__(self):
                return self.description

class Course(models.Model):
        title=models.TextField(blank=False)
        number=models.IntegerField(unique=True,blank=False)
        department=models.ForeignKey(Department,blank=False,on_delete=models.PROTECT)
        def __str__(self):
                return self.department.name+' '+str(self.number) + ' - ' + self.title

class Semester(models.Model):
        name=models.CharField(max_length=10,blank=False)
        year=models.IntegerField(blank=False)
        def __str__(self):
                return self.name + ' ' + str(self.year)

class Section(models.Model):
        course=models.ForeignKey(Course,blank=False,on_delete=models.PROTECT)
        number=models.CharField(max_length=10,blank=False)
        semester=models.ForeignKey(Semester,blank=False,on_delete=models.PROTECT)
        def get_absolute_url(self):
                return resolve_url('grades:section',section_id=self.id)
        def __str__(self):
                return str(self.number) + ' (' + str(self.course) + ' - ' + str(self.semester) + ')'

class Assignment(models.Model):
        section=models.ForeignKey(Section,blank=False,on_delete=models.PROTECT)
        name=models.CharField(max_length=50,blank=False)
        max_value=models.FloatField(default=100)
        assign_date=models.DateField(null=True,blank=True)
        due_date=models.DateField(null=True,blank=True)
        assignment_type=models.ForeignKey(AssignmentType,blank=False,on_delete=models.PROTECT)
        a_cutoff=models.FloatField(null=True,blank=True)
        b_cutoff=models.FloatField(null=True,blank=True)
        c_cutoff=models.FloatField(null=True,blank=True)
        d_cutoff=models.FloatField(null=True,blank=True)
        def __str__(self):
                return self.name + ' (Section ' + self.section.number +')'
        class Meta:
                unique_together=('section','name')

class Student(models.Model):
        id=models.IntegerField(primary_key=True,unique=True,blank=False)
        last_name=models.CharField(max_length=50,blank=False)
        first_name=models.CharField(max_length=50,blank=False)
        middle_name=models.CharField(max_length=20,null=True,blank=True)
        nick_name=models.CharField(max_length=50,null=True,blank=True)
        phone=models.CharField(max_length=50,null=True,blank=True)
        email=models.CharField(max_length=200,null=True,blank=True)
        suffix=models.CharField(max_length=10,null=True,blank=True)
        def __str__(self):
                return self.last_name + ', ' + self.first_name + ' (' + str(self.id) + ')'

class AssignmentScore(models.Model):
        student=models.ForeignKey(Student,blank=False,on_delete=models.PROTECT)
        assignment=models.ForeignKey(Assignment,blank=False,on_delete=models.PROTECT)
        score=models.FloatField(null=True,blank=True)
        def get_letter_grade(self):
                if(self.assignment.a_cutoff):
                        if(self.score>self.assignment.a_cutoff):
                                return "A"
                        if(self.score>self.assignment.b_cutoff):
                                return "B"
                        if(self.score>self.assignment.c_cutoff):
                                return "C"
                        if(self.score>self.assignment.d_cutoff):
                                return "D"
                        return "F"
                return ""
        def __str__(self):
                return 'Assignment: '+str(self.assignment) + ', Student: ' + str(self.student)
        class Meta:
                unique_together=('student','assignment')

class Roster(models.Model):
        section=models.ForeignKey(Section,blank=False,on_delete=models.PROTECT)
        student=models.ForeignKey(Student,blank=False,on_delete=models.PROTECT)
        enrollment_status=models.ForeignKey(EnrollmentStatus,blank=False,on_delete=models.PROTECT)
        def get_absolute_url(self):
                return resolve_url('grades:roster_student',section_id=self.section.id,student_id=self.student.id)
        def __str__(self):
                return str(self.section) + '/' + str(self.student)
        class Meta:
                unique_together=('section','student')

class Attendance(models.Model):
        student=models.ForeignKey(Student,blank=False,on_delete=models.PROTECT)
        section=models.ForeignKey(Section,blank=False,on_delete=models.PROTECT)
        date=models.DateField(blank=False)
        def __str__(self):
                return 'Section '+self.section.number+' - '+str(self.student) + ' - ' + str(self.date)

class PermissionCode(models.Model):
        permission_code=models.IntegerField(blank=False)
        section=models.ForeignKey(Section,blank=False)
        student=models.ForeignKey(Student,null=True,blank=True)
        def __str__(self):
                return 'Section '+self.section.number + ': ' + str(self.permission_code)
