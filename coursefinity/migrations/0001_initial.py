# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Link'
        db.create_table(u'coursefinity_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=250)),
        ))
        db.send_create_signal(u'coursefinity', ['Link'])

        # Adding model 'Career'
        db.create_table(u'coursefinity_career', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'coursefinity', ['Career'])

        # Adding model 'Program'
        db.create_table(u'coursefinity_program', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('career', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coursefinity.Career'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'coursefinity', ['Program'])

        # Adding model 'Courses'
        db.create_table(u'coursefinity_courses', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coursefinity.Program'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'coursefinity', ['Courses'])


    def backwards(self, orm):
        # Deleting model 'Link'
        db.delete_table(u'coursefinity_link')

        # Deleting model 'Career'
        db.delete_table(u'coursefinity_career')

        # Deleting model 'Program'
        db.delete_table(u'coursefinity_program')

        # Deleting model 'Courses'
        db.delete_table(u'coursefinity_courses')


    models = {
        u'coursefinity.career': {
            'Meta': {'object_name': 'Career'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'coursefinity.courses': {
            'Meta': {'object_name': 'Courses'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coursefinity.Program']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'coursefinity.link': {
            'Meta': {'object_name': 'Link'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '250'})
        },
        u'coursefinity.program': {
            'Meta': {'object_name': 'Program'},
            'career': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coursefinity.Career']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['coursefinity']