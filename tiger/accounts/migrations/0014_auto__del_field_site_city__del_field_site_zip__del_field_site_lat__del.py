# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Site.city'
        db.delete_column('accounts_site', 'city')

        # Deleting field 'Site.zip'
        db.delete_column('accounts_site', 'zip')

        # Deleting field 'Site.lat'
        db.delete_column('accounts_site', 'lat')

        # Deleting field 'Site.phone'
        db.delete_column('accounts_site', 'phone')

        # Deleting field 'Site.lon'
        db.delete_column('accounts_site', 'lon')

        # Deleting field 'Site.enable_blog'
        db.delete_column('accounts_site', 'enable_blog')

        # Deleting field 'Site.blog_address'
        db.delete_column('accounts_site', 'blog_address')

        # Deleting field 'Site.state'
        db.delete_column('accounts_site', 'state')

        # Deleting field 'Site.street'
        db.delete_column('accounts_site', 'street')

        # Deleting field 'Site.timezone'
        db.delete_column('accounts_site', 'timezone')

        # Deleting field 'Site.fax_number'
        db.delete_column('accounts_site', 'fax_number')

        # Adding field 'Location.delivery_area'
        db.add_column('accounts_location', 'delivery_area', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Site.city'
        db.add_column('accounts_site', 'city', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'Site.zip'
        db.add_column('accounts_site', 'zip', self.gf('django.db.models.fields.CharField')(default='', max_length=10), keep_default=False)

        # Adding field 'Site.lat'
        db.add_column('accounts_site', 'lat', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=9), keep_default=False)

        # Adding field 'Site.phone'
        db.add_column('accounts_site', 'phone', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(default='', max_length=20), keep_default=False)

        # Adding field 'Site.lon'
        db.add_column('accounts_site', 'lon', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=9), keep_default=False)

        # Adding field 'Site.enable_blog'
        db.add_column('accounts_site', 'enable_blog', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True), keep_default=False)

        # Adding field 'Site.blog_address'
        db.add_column('accounts_site', 'blog_address', self.gf('django.db.models.fields.URLField')(default=1, max_length=200, blank=True), keep_default=False)

        # Adding field 'Site.state'
        db.add_column('accounts_site', 'state', self.gf('django.contrib.localflavor.us.models.USStateField')(default='', max_length=2), keep_default=False)

        # Adding field 'Site.street'
        db.add_column('accounts_site', 'street', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'Site.timezone'
        db.add_column('accounts_site', 'timezone', self.gf('django.db.models.fields.CharField')(default='US/Eastern', max_length=100), keep_default=False)

        # Adding field 'Site.fax_number'
        db.add_column('accounts_site', 'fax_number', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(default='', max_length=20, blank=True), keep_default=False)

        # Deleting field 'Location.delivery_area'
        db.delete_column('accounts_location', 'delivery_area')


    models = {
        'accounts.account': {
            'Meta': {'object_name': 'Account'},
            'card_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'card_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'customer_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fax': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'referrer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.SalesRep']", 'null': 'True'}),
            'signup_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'subscription_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'accounts.faxlist': {
            'Meta': {'object_name': 'FaxList'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Site']"})
        },
        'accounts.location': {
            'Meta': {'object_name': 'Location'},
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'delivery_area': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fax_number': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '9'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '9'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'phone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'default': "''", 'max_length': '20'}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Schedule']"}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Site']"}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'default': "''", 'max_length': '2'}),
            'street': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'timezone': ('django.db.models.fields.CharField', [], {'default': "'US/Eastern'", 'max_length': '100'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'})
        },
        'accounts.salesrep': {
            'Meta': {'object_name': 'SalesRep'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plan': ('django.db.models.fields.CharField', [], {'default': "'chomp3'", 'max_length': '12'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'accounts.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'display': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'master': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Site']"})
        },
        'accounts.site': {
            'Meta': {'object_name': 'Site'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Account']"}),
            'custom_domain': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'enable_orders': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Your Restaurant Name'", 'max_length': '200'}),
            'subdomain': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'walkthrough_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'})
        },
        'accounts.subscriber': {
            'Meta': {'object_name': 'Subscriber'},
            'fax': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'fax_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.FaxList']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'accounts.timeslot': {
            'Meta': {'object_name': 'TimeSlot'},
            'dow': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Schedule']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Section']", 'null': 'True'}),
            'start': ('django.db.models.fields.TimeField', [], {}),
            'stop': ('django.db.models.fields.TimeField', [], {})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.section': {
            'Meta': {'object_name': 'Section'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ordering': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Schedule']", 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['accounts']
