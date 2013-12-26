from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gradebook.views.home', name='home'),
    # url(r'^gradebook/', include('gradebook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^grades/', include('grades.urls', namespace="grades")),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'grades/login.html'}),
    url(r'^foundation/',include('foundation.urls')),
)
