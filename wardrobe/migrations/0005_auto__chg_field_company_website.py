# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Company.website'
        db.alter_column(u'wardrobe_company', 'website', self.gf('django.db.models.fields.URLField')(max_length=500, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Company.website'
        raise RuntimeError("Cannot reverse this migration. 'Company.website' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Company.website'
        db.alter_column(u'wardrobe_company', 'website', self.gf('django.db.models.fields.URLField')(max_length=500))

    models = {
        u'wardrobe.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wardrobe.Category']", 'null': 'True', 'blank': 'True'})
        },
        u'wardrobe.company': {
            'Meta': {'object_name': 'Company'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        u'wardrobe.item': {
            'Meta': {'object_name': 'Item'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': u"orm['wardrobe.Category']"}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'items'", 'null': 'True', 'to': u"orm['wardrobe.Company']"}),
            'cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'purchased_from': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'wardrobe.itemimage': {
            'Meta': {'object_name': 'ItemImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['wardrobe.Item']"})
        }
    }

    complete_apps = ['wardrobe']