from django.db import models


class EnrollmentStatus(models.Model):
	description=models.TextField(unique=True,blank=False)
	
class AssignmentType(models.Model):
	description=models.TextField(unique=True,blank=False)

class Course(models.Model):
	title=models.TextField(blank=False)
	number=models.IntegerField(unique=True,blank=False)

class Semester(models.Model):
	name=models.TextField(blank=False)
	year=models.IntegerField(blank=False)

class Section(models.Model):
	course=models.ForeignKey(Course,blank=False,on_delete=models.PROTECT)
	number=models.TextField(blank=False)
	semester=models.ForeignKey(Semester,blank=False,on_delete=models.PROTECT)

class Assignment(models.Model):
	section=models.ForeignKey(Section,blank=False,on_delete=models.PROTECT)
	name=models.TextField(blank=False)
	max_value=models.FloatField(default=100)
	assignment_type=models.ForeignKey(AssignmentType,blank=False,on_delete=models.PROTECT)
        class Meta:
                unique_together=('section','name')

class Student(models.Model):
	id=models.IntegerField(primary_key=True,unique=True,blank=False)
	last_name=models.TextField(blank=False)
	first_name=models.TextField(blank=False)
	middle_name=models.TextField(null=True)
	nick_name=models.TextField(null=True)
	phone=models.TextField(null=True)
	email=models.TextField(null=True)
	suffix=models.TextField(null=True)

class AssignmentScore(models.Model):
	student=models.ForeignKey(Student,blank=False,on_delete=models.PROTECT)
	assignment=models.ForeignKey(Assignment,blank=False,on_delete=models.PROTECT)
	score=models.FloatField(null=True)
        class Meta:
                unique_together=('student','assignment')

class Roster(models.Model):
	section=models.ForeignKey(Section,blank=False,on_delete=models.PROTECT)
	student=models.ForeignKey(Student,blank=False,on_delete=models.PROTECT)
	enrollment_status=models.ForeignKey(EnrollmentStatus,blank=False,on_delete=models.PROTECT)
        class Meta:
                unique_together=('section','student')

class Attendance(models.Model):
	student=models.ForeignKey(Student,blank=False,on_delete=models.PROTECT)
	section=models.ForeignKey(Section,blank=False,on_delete=models.PROTECT)
	date=models.DateField(blank=False)

class PermissionCodes(models.Model):
	permission_code=models.IntegerField(blank=False)
	section=models.ForeignKey(Section,blank=False)
	student=models.ForeignKey(Student,null=True)

