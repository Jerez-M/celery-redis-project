# Generated by Django 5.0 on 2024-01-03 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_name', models.CharField(blank=True, max_length=200, null=True)),
                ('organisation_code', models.CharField(blank=True, default='GI', max_length=10, null=True)),
                ('organisation_type', models.CharField(blank=True, choices=[('NON GOVERNMENTAL ORGANIZATION', 'NON GOVERNMENTAL ORGANIZATION'), ('INTERNATIONAL NON-GOVERNMENTAL ORGANIZATION', 'INTERNATIONAL NON-GOVERNMENTAL ORGANIZATION'), ('COMMUNITY-BASED ORGANIZATION', 'COMMUNITY-BASED ORGANIZATION'), ('GOVERNMENTAL ORGANIZATION', 'GOVERNMENTAL ORGANIZATION'), ('SOCIAL ENTERPRISE', 'SOCIAL ENTERPRISE'), ('FOUNDATION', 'FOUNDATION'), ('HEALTHCARE ORGANIZATION', 'HEALTHCARE ORGANIZATION')], max_length=250, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=25, null=True)),
                ('organisation_address', models.TextField(blank=True, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('district', models.CharField(blank=True, max_length=50, null=True)),
                ('province', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('logo', models.ImageField(blank=True, default='organisation_logos/default_logo.jpg', null=True, upload_to='organisation_logos')),
                ('active', models.BooleanField(default=True, help_text='active is a boolean field, can either be Tue or False')),
                ('organisation_number', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
    ]
