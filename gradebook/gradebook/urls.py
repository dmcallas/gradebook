from django.conf.urls import patterns, include, url
from rest_framework import routers
from grades import views

from django.contrib import admin

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'department', views.DepartmentViewSet)
router.register(r'enrollment_status', views.EnrollmentStatusViewSet)
router.register(r'assignment_type', views.AssignmentTypeViewSet)
router.register(r'course', views.CourseViewSet)
router.register(r'semester', views.SemesterViewSet)
router.register(r'section', views.SectionViewSet)
router.register(r'assignment', views.AssignmentViewSet)
router.register(r'student', views.StudentViewSet)
router.register(r'assignment_score', views.AssignmentScoreViewSet)
router.register(r'roster', views.RosterViewSet)
router.register(r'attendance', views.AttendanceViewSet)
router.register(r'permission_code', views.PermissionCodeViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gradebook.views.home', name='home'),
    # url(r'^gradebook/', include('gradebook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^grades/', include('grades.urls', namespace="grades")),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'grades/login.html'}, name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),

    # ZURB Foundation
    url(r'^foundation/',include('foundation.urls')),
    # REST API
    url(r'^rest/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
