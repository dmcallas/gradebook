from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets, permissions

from grades.serializers import *
from grades.models import *

def index(request):
    return render(request, 'grades/index.html')

def section_index(request):
    section_list = list(Section.objects.all())
    return render(request, 'grades/section/index.html', {'section_list': section_list})

def section(request,section_id):
    section = get_object_or_404(Section,pk=section_id)
    return render(request, 'grades/section/section.html', {'section': section})

@login_required
def roster(request,section_id):
    privacy=(request.GET.get('p', 'false')=='true')
    section = get_object_or_404(Section,pk=section_id)
    if privacy:
        enrolled=get_object_or_404(EnrollmentStatus,description='ENROLLED')
        roster = list(Roster.objects.filter(section=section_id).filter(enrollment_status=enrolled).order_by('student__last_name','student__first_name'))
    else:
        roster = list(Roster.objects.filter(section=section_id).order_by('student__last_name','student__first_name'))
    enrollment_statuses = list(EnrollmentStatus.objects.all())

    return render(request, 'grades/roster/roster.html', {'roster': roster,'section': section,'enrollment_statuses':enrollment_statuses,'privacy':privacy})

def assignments(request,section_id):
    section = get_object_or_404(Section,pk=section_id)
    assignments = list(Assignment.objects.filter(section=section_id));
    return render(request, 'grades/assignments/assignments.html', {'assignments': assignments,'section': section})

@login_required
def roster_student(request,section_id,student_id):
    privacy=(request.GET.get('p', 'false')=='true')
    section = get_object_or_404(Section,pk=section_id)
    assignment_scores = list(AssignmentScore.objects.filter(student=student_id).order_by('assignment__name'))
    student = get_object_or_404(Student,pk=student_id)
    roster = get_object_or_404(Roster,student=student_id,section=section_id)
    return render(request, 'grades/roster/roster_student.html', {'assignment_scores': assignment_scores,'section': section,'student':student,'roster':roster,'privacy':privacy})

@login_required
def hw_entry(request,section_id):
    enrolled_status = EnrollmentStatus.objects.filter(description='ENROLLED')
    hw_type = AssignmentType.objects.get(description='Homework')
    section = get_object_or_404(Section,pk=section_id)
    hw_assignments = list(Assignment.objects.filter(section=section_id,assignment_type=hw_type).order_by('due_date').order_by('name'))
    roster = list(Roster.objects.filter(section=section_id).filter(enrollment_status=enrolled_status).order_by('student__last_name','student__first_name'))
    scores = AssignmentScore.objects.filter(assignment__section=section_id).filter(assignment__assignment_type__description='Homework').filter(assignment__max_value=1.0)
    return render(request, 'grades/entry/homework.html',{'section':section,'hw_assignments':hw_assignments,'roster':roster,'scores':scores})

@login_required
@require_http_methods(["POST", "DELETE"])
def hw_assignment_add_remove(request,section_id,student_id,assignment_id):
    student=get_object_or_404(Student,id=student_id)
    assignment=get_object_or_404(Assignment,id=assignment_id)
    if request.method=='POST':
        assignment_score=AssignmentScore(student=student,assignment=assignment,score=1.0)
        assignment_score.save()
        return HttpResponse("Added")
    if request.method=='DELETE':
        AssignmentScore.objects.filter(student=student,assignment=assignment,score=1.0).delete()
        return HttpResponse("Deleted")

@login_required
def view_scores(request,section_id):
    enrolled_status = EnrollmentStatus.objects.filter(description='ENROLLED')
    section = get_object_or_404(Section,pk=section_id)
    assignments = list(Assignment.objects.filter(section=section_id).order_by('assignment_type').order_by('due_date').order_by('name'))
    roster = list(Roster.objects.filter(section=section_id).filter(enrollment_status=enrolled_status).order_by('student__last_name','student__first_name'))
    scores = AssignmentScore.objects.filter(assignment__section=section_id)
    return render(request, 'grades/view/all.html',{'section':section,'assignments':assignments,'roster':roster,'scores':scores})


##################################################
#                 Views for REST                 #
##################################################

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class EnrollmentStatusViewSet(viewsets.ModelViewSet):
    queryset = EnrollmentStatus.objects.all()
    serializer_class = EnrollmentStatusSerializer
    permission_classes = (permissions.IsAuthenticated,)

class AssignmentTypeViewSet(viewsets.ModelViewSet):
    queryset = AssignmentType.objects.all()
    serializer_class = AssignmentTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_fields = ('department',)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    filter_fields = ('course','semester',)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    filter_fields = ('assignment_type','section',)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_fields = ('last_name', 'first_name',)
    permission_classes = (permissions.IsAuthenticated,)

class AssignmentScoreViewSet(viewsets.ModelViewSet):
    queryset = AssignmentScore.objects.all()
    serializer_class = AssignmentScoreSerializer
    filter_fields = ('student','assignment',)
    permission_classes = (permissions.IsAuthenticated,)

class RosterViewSet(viewsets.ModelViewSet):
    queryset = Roster.objects.all()
    serializer_class = RosterSerializer
    filter_fields = ('section','student','enrollment_status',)
    permission_classes = (permissions.IsAuthenticated,)

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_fields = ('section','student',)
    permission_classes = (permissions.IsAuthenticated,)

class PermissionCodeViewSet(viewsets.ModelViewSet):
    queryset = PermissionCode.objects.all()
    serializer_class = PermissionCodeSerializer
    filter_fields = ('section',)
    permission_classes = (permissions.IsAuthenticated,)
