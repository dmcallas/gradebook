from django.db import models


class EnrollmentStatus(models.Model):
	description=models.TextField(unique=True,blank=False)
	def __unicode__(self):
                return self.description

class AssignmentType(models.Model):
	description=models.TextField(unique=True,blank=False)
	def __unicode__(self):
                return self.description

class Course(models.Model):
	title=models.TextField(blank=False)
	number=models.IntegerField(unique=True,blank=False)
	def __unicode__(self):
                return unicode(self.number) + ' - ' + self.title

class Semester(models.Model):
	name=models.TextField(blank=False)
	year=models.IntegerField(blank=False)
	def __unicode__(self):
                return self.name + ' ' + unicode(self.year)

class Section(models.Model):
	course=models.ForeignKey(Course,blank=False,on_delete=models.PROTECT)
	number=models.TextField(blank=False)
	semester=models.ForeignKey(Semester,blank=False,on_delete=models.PROTECT)
	def __unicode__(self):
                return unicode(self.number) + ' (' + unicode(self.course) + ' - ' + unicode(self.semester) + ')'

class Assignment(models.Model):
	section=models.ForeignKey(Section,blank=False,on_delete=models.PROTECT)
	name=models.TextField(blank=False)
	max_value=models.FloatField(default=100)
	assignment_type=models.ForeignKey(AssignmentType,blank=False,on_delete=models.PROTECT)
	def __unicode__(self):
                return self.name + ' (Section ' + self.section.number +')'
        class Meta:
                unique_together=('section','name')

class Student(models.Model):
	id=models.IntegerField(primary_key=True,unique=True,blank=False)
	last_name=models.TextField(blank=False)
	first_name=models.TextField(blank=False)
	middle_name=models.TextField(null=True,blank=True)
	nick_name=models.TextField(null=True,blank=True)
	phone=models.TextField(null=True,blank=True)
	email=models.TextField(null=True,blank=True)
	suffix=models.TextField(null=True,blank=True)
	def __unicode__(self):
                return self.last_name + ', ' + self.first_name + ' (' + unicode(self.id) + ')'


class AssignmentScore(models.Model):
	student=models.ForeignKey(Student,blank=False,on_delete=models.PROTECT)
	assignment=models.ForeignKey(Assignment,blank=False,on_delete=models.PROTECT)
	score=models.FloatField(null=True,blank=True)
	def __unicode__(self):
                return 'Assignment: '+unicode(self.assignment) + ', Student: ' + unicode(self.student)
        class Meta:
                unique_together=('student','assignment')

class Roster(models.Model):
	section=models.ForeignKey(Section,blank=False,on_delete=models.PROTECT)
	student=models.ForeignKey(Student,blank=False,on_delete=models.PROTECT)
	enrollment_status=models.ForeignKey(EnrollmentStatus,blank=False,on_delete=models.PROTECT)
	def __unicode__(self):
                return unicode(self.section) + '/' + unicode(self.student)
        class Meta:
                unique_together=('section','student')

class Attendance(models.Model):
	student=models.ForeignKey(Student,blank=False,on_delete=models.PROTECT)
	section=models.ForeignKey(Section,blank=False,on_delete=models.PROTECT)
	date=models.DateField(blank=False)
	def __unicode__(self):
                return 'Section '+self.section.number+' - '+unicode(self.student) + ' - ' + unicode(self.date)

class PermissionCode(models.Model):
	permission_code=models.IntegerField(blank=False)
	section=models.ForeignKey(Section,blank=False)
	student=models.ForeignKey(Student,null=True,blank=True)
	def __unicode__(self):
                return 'Section '+self.section.number + ': ' + unicode(self.permission_code)

