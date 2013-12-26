from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required

from grades.models import *

def index(request):
    return render(request, 'grades/index.html')

def section_index(request):
    section_list = get_list_or_404(Section)
    return render(request, 'grades/section/index.html', {'section_list': section_list})

def section(request,section_id):
    section = get_object_or_404(Section,pk=section_id)
    return render(request, 'grades/section/section.html', {'section': section})

@login_required
def roster(request,section_id):
    section = get_object_or_404(Section,pk=section_id)
    roster = get_list_or_404(Roster,section=section_id)
    return render(request, 'grades/roster/roster.html', {'roster': roster,'section': section})

def assignments(request,section_id):
    section = get_object_or_404(Section,pk=section_id)
    assignments = get_list_or_404(Assignment,section=section_id)
    return render(request, 'grades/assignments/assignments.html', {'assignments': assignments,'section': section})

def roster_student(request,section_id,student_id):
    section = get_object_or_404(Section,pk=section_id)
    assignment_scores = list(AssignmentScore.objects.filter(student=student_id))
    student = get_object_or_404(Student,pk=student_id)
    roster = get_object_or_404(Roster,student=student_id,section=section_id)
    return render(request, 'grades/roster/roster_student.html', {'assignment_scores': assignment_scores,'section': section,'student':student,'roster':roster})

def hw_entry(request,section_id):
    enrolled_status = get_object_or_404(EnrollmentStatus,description='ENROLLED')
    hw_type = get_object_or_404(AssignmentType,description='Homework')
    section = get_object_or_404(Section,pk=section_id)
    hw_assignments = get_list_or_404(Assignment,section=section_id,assignment_type=hw_type)
    roster = get_list_or_404(Roster,section=section_id,enrollment_status=enrolled_status)
    return render(request, 'grades/entry/homework.html',{'section':section,'hw_assignments':hw_assignments,'roster':roster})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
