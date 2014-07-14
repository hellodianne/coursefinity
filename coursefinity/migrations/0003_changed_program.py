# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Program.career'
        db.delete_column(u'coursefinity_program', 'career_id')

        # Adding M2M table for field career on 'Program'
        m2m_table_name = db.shorten_name(u'coursefinity_program_career')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('program', models.ForeignKey(orm[u'coursefinity.program'], null=False)),
            ('career', models.ForeignKey(orm[u'coursefinity.career'], null=False))
        ))
        db.create_unique(m2m_table_name, ['program_id', 'career_id'])


    def backwards(self, orm):
        # Adding field 'Program.career'
        db.add_column(u'coursefinity_program', 'career',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=datetime.datetime(2014, 7, 14, 0, 0), to=orm['coursefinity.Career']),
                      keep_default=False)

        # Removing M2M table for field career on 'Program'
        db.delete_table(db.shorten_name(u'coursefinity_program_career'))


    models = {
        u'coursefinity.career': {
            'Meta': {'object_name': 'Career'},
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'coursefinity.courses': {
            'Meta': {'object_name': 'Courses'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
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
            'career': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['coursefinity.Career']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['coursefinity']