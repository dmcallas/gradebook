# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Department'
        db.create_table(u'grades_department', (
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10, primary_key=True)),
            ('long_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'grades', ['Department'])

        # Adding model 'EnrollmentStatus'
        db.create_table(u'grades_enrollmentstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
        ))
        db.send_create_signal(u'grades', ['EnrollmentStatus'])

        # Adding model 'AssignmentType'
        db.create_table(u'grades_assignmenttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')(unique=True)),
        ))
        db.send_create_signal(u'grades', ['AssignmentType'])

        # Adding model 'Course'
        db.create_table(u'grades_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('number', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grades.Department'], on_delete=models.PROTECT)),
        ))
        db.send_create_signal(u'grades', ['Course'])

        # Adding model 'Semester'
        db.create_table(u'grades_semester', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'grades', ['Semester'])

        # Adding model 'Section'
        db.create_table(u'grades_section', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grades.Course'], on_delete=models.PROTECT)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('semester', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grades.Semester'], on_delete=models.PROTECT)),
        ))
        db.send_create_signal(u'grades', ['Section'])

        # Adding model 'Assignment'
        db.create_table(u'grades_assignment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grades.Section'], on_delete=models.PROTECT)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('max_value', self.gf('django.db.models.fields.FloatField')(default=100)),
            ('assign_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('due_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('assignment_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grades.AssignmentType'], on_delete=models.PROTECT)),
            ('a_cutoff', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('b_cutoff', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('c_cutoff', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('d_cutoff', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'grades', ['Assignment'])

        # Adding unique constraint on 'Assignment', fields ['section', 'name']
        db.create_unique(u'grades_assignment', ['section_id', 'name'])

        # Adding model 'Student'
        db.create_table(u'grades_student', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('nick_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('suffix', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal(u'grades', ['Student'])

        # Adding model 'AssignmentScore'
        db.create_table(u'grades_assignmentscore', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grades.Student'], on_delete=models.PROTECT)),
            ('assignment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grades.Assignment'], on_delete=models.PROTECT)),
            ('score', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'grades', ['AssignmentScore'])

        # Adding unique constraint on 'AssignmentScore', fields ['student', 'assignment']
        db.create_unique(u'grades_assignmentscore', ['student_id', 'assignment_id'])

        # Adding model 'Roster'
        db.create_table(u'grades_roster', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grades.Section'], on_delete=models.PROTECT)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grades.Student'], on_delete=models.PROTECT)),
            ('enrollment_status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grades.EnrollmentStatus'], on_delete=models.PROTECT)),
        ))
        db.send_create_signal(u'grades', ['Roster'])

        # Adding unique constraint on 'Roster', fields ['section', 'student']
        db.create_unique(u'grades_roster', ['section_id', 'student_id'])

        # Adding model 'Attendance'
        db.create_table(u'grades_attendance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grades.Student'], on_delete=models.PROTECT)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grades.Section'], on_delete=models.PROTECT)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'grades', ['Attendance'])

        # Adding model 'PermissionCode'
        db.create_table(u'grades_permissioncode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('permission_code', self.gf('django.db.models.fields.IntegerField')()),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grades.Section'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grades.Student'], null=True, blank=True)),
        ))
        db.send_create_signal(u'grades', ['PermissionCode'])


    def backwards(self, orm):
        # Removing unique constraint on 'Roster', fields ['section', 'student']
        db.delete_unique(u'grades_roster', ['section_id', 'student_id'])

        # Removing unique constraint on 'AssignmentScore', fields ['student', 'assignment']
        db.delete_unique(u'grades_assignmentscore', ['student_id', 'assignment_id'])

        # Removing unique constraint on 'Assignment', fields ['section', 'name']
        db.delete_unique(u'grades_assignment', ['section_id', 'name'])

        # Deleting model 'Department'
        db.delete_table(u'grades_department')

        # Deleting model 'EnrollmentStatus'
        db.delete_table(u'grades_enrollmentstatus')

        # Deleting model 'AssignmentType'
        db.delete_table(u'grades_assignmenttype')

        # Deleting model 'Course'
        db.delete_table(u'grades_course')

        # Deleting model 'Semester'
        db.delete_table(u'grades_semester')

        # Deleting model 'Section'
        db.delete_table(u'grades_section')

        # Deleting model 'Assignment'
        db.delete_table(u'grades_assignment')

        # Deleting model 'Student'
        db.delete_table(u'grades_student')

        # Deleting model 'AssignmentScore'
        db.delete_table(u'grades_assignmentscore')

        # Deleting model 'Roster'
        db.delete_table(u'grades_roster')

        # Deleting model 'Attendance'
        db.delete_table(u'grades_attendance')

        # Deleting model 'PermissionCode'
        db.delete_table(u'grades_permissioncode')


    models = {
        u'grades.assignment': {
            'Meta': {'unique_together': "(('section', 'name'),)", 'object_name': 'Assignment'},
            'a_cutoff': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'assign_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'assignment_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['grades.AssignmentType']", 'on_delete': 'models.PROTECT'}),
            'b_cutoff': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'c_cutoff': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'd_cutoff': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_value': ('django.db.models.fields.FloatField', [], {'default': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['grades.Section']", 'on_delete': 'models.PROTECT'})
        },
        u'grades.assignmentscore': {
            'Meta': {'unique_together': "(('student', 'assignment'),)", 'object_name': 'AssignmentScore'},
            'assignment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['grades.Assignment']", 'on_delete': 'models.PROTECT'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['grades.Student']", 'on_delete': 'models.PROTECT'})
        },
        u'grades.assignmenttype': {
            'Meta': {'object_name': 'AssignmentType'},
            'description': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'grades.attendance': {
            'Meta': {'object_name': 'Attendance'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['grades.Section']", 'on_delete': 'models.PROTECT'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['grades.Student']", 'on_delete': 'models.PROTECT'})
        },
        u'grades.course': {
            'Meta': {'object_name': 'Course'},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['grades.Department']", 'on_delete': 'models.PROTECT'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'grades.department': {
            'Meta': {'object_name': 'Department'},
            'long_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10', 'primary_key': 'True'})
        },
        u'grades.enrollmentstatus': {
            'Meta': {'object_name': 'EnrollmentStatus'},
            'description': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'grades.permissioncode': {
            'Meta': {'object_name': 'PermissionCode'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'permission_code': ('django.db.models.fields.IntegerField', [], {}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['grades.Section']"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['grades.Student']", 'null': 'True', 'blank': 'True'})
        },
        u'grades.roster': {
            'Meta': {'unique_together': "(('section', 'student'),)", 'object_name': 'Roster'},
            'enrollment_status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['grades.EnrollmentStatus']", 'on_delete': 'models.PROTECT'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['grades.Section']", 'on_delete': 'models.PROTECT'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['grades.Student']", 'on_delete': 'models.PROTECT'})
        },
        u'grades.section': {
            'Meta': {'object_name': 'Section'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['grades.Course']", 'on_delete': 'models.PROTECT'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'semester': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['grades.Semester']", 'on_delete': 'models.PROTECT'})
        },
        u'grades.semester': {
            'Meta': {'object_name': 'Semester'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'grades.student': {
            'Meta': {'object_name': 'Student'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'nick_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['grades']