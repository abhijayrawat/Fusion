# Generated by Django 3.1.5 on 2024-07-16 15:44

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academic_information', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChairmanVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='', max_length=100)),
                ('location', models.CharField(default='', max_length=100)),
                ('visiting_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('description', models.TextField(blank=True, default='', max_length=1000, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MessageOfficer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(default='', max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='NotifyStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placement_type', models.CharField(choices=[('PLACEMENT', 'Placement'), ('PBI', 'PBI'), ('HIGHER STUDIES', 'Higher Studies'), ('OTHER', 'Other')], default='PLACEMENT', max_length=20)),
                ('company_name', models.CharField(default='', max_length=100)),
                ('ctc', models.DecimalField(decimal_places=4, max_digits=10)),
                ('description', models.TextField(blank=True, default='', max_length=1000, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlacementRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placement_type', models.CharField(choices=[('PLACEMENT', 'Placement'), ('PBI', 'PBI'), ('HIGHER STUDIES', 'Higher Studies'), ('OTHER', 'Other')], default='PLACEMENT', max_length=20)),
                ('name', models.CharField(default='', max_length=100)),
                ('ctc', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('year', models.IntegerField(default=0)),
                ('test_score', models.IntegerField(blank=True, default=0, null=True)),
                ('test_type', models.CharField(blank=True, default='', max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='StudentPlacement',
            fields=[
                ('unique_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='academic_information.student')),
                ('debar', models.CharField(choices=[('NOT DEBAR', 'Not Debar'), ('DEBAR', 'Debar')], default='NOT DEBAR', max_length=20)),
                ('future_aspect', models.CharField(choices=[('PLACEMENT', 'Placement'), ('PBI', 'PBI'), ('HIGHER STUDIES', 'Higher Studies'), ('OTHER', 'Other')], default='PLACEMENT', max_length=20)),
                ('placed_type', models.CharField(choices=[('NOT PLACED', 'Not Placed'), ('PLACED', 'Placed')], default='NOT PLACED', max_length=20)),
                ('placement_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Date')),
                ('package', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_name', models.CharField(default='', max_length=100)),
                ('post', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('email', models.CharField(default='', max_length=50)),
                ('mobile_number', models.CharField(blank=True, max_length=15, null=True)),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_title', models.CharField(default='', max_length=100)),
                ('description', models.TextField(blank=True, default='', max_length=250, null=True)),
                ('publisher', models.TextField(default='', max_length=250)),
                ('publication_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(default='', max_length=50)),
                ('project_status', models.CharField(choices=[('ONGOING', 'Ongoing'), ('COMPLETED', 'Completed')], default='COMPLETED', max_length=20)),
                ('summary', models.TextField(blank=True, default='', max_length=1000, null=True)),
                ('project_link', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('sdate', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('edate', models.DateField(blank=True, null=True)),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='PlacementSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('placement_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('location', models.CharField(default='', max_length=100)),
                ('description', models.TextField(blank=True, default='', max_length=500, null=True)),
                ('time', models.TimeField()),
                ('attached_file', models.FileField(blank=True, null=True, upload_to='documents/placement/schedule')),
                ('schedule_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('notify_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placement_cell.notifystudent')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='placement_cell.role')),
            ],
        ),
        migrations.CreateModel(
            name='Patent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patent_name', models.CharField(default='', max_length=100)),
                ('description', models.TextField(blank=True, default='', max_length=250, null=True)),
                ('patent_office', models.TextField(default='', max_length=250)),
                ('patent_date', models.DateField()),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(default='', max_length=100)),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='Extracurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(default='', max_length=100)),
                ('event_type', models.CharField(choices=[('SOCIAL', 'Social'), ('CULTURE', 'Culture'), ('SPORT', 'Sport'), ('OTHER', 'Other')], default='OTHER', max_length=20)),
                ('description', models.TextField(blank=True, default='', max_length=1000, null=True)),
                ('name_of_position', models.CharField(default='', max_length=200)),
                ('date_earned', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('status', models.CharField(choices=[('ONGOING', 'Ongoing'), ('COMPLETED', 'Completed')], default='COMPLETED', max_length=20)),
                ('description', models.TextField(blank=True, default='', max_length=500, null=True)),
                ('company', models.CharField(default='', max_length=200)),
                ('location', models.CharField(default='', max_length=200)),
                ('sdate', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('edate', models.DateField(blank=True, null=True)),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(default='', max_length=40)),
                ('grade', models.CharField(default='', max_length=10)),
                ('institute', models.TextField(default='', max_length=250)),
                ('stream', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('sdate', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('edate', models.DateField(blank=True, null=True)),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(default='', max_length=100)),
                ('description', models.TextField(blank=True, default='', max_length=250, null=True)),
                ('license_no', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('sdate', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('edate', models.DateField(blank=True, null=True)),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conference_name', models.CharField(default='', max_length=100)),
                ('description', models.TextField(blank=True, default='', max_length=250, null=True)),
                ('sdate', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('edate', models.DateField(blank=True, null=True)),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='Coinventor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coinventor_name', models.CharField(default='', max_length=100)),
                ('patent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placement_cell.patent')),
            ],
        ),
        migrations.CreateModel(
            name='Coauthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coauthor_name', models.CharField(default='', max_length=100)),
                ('publication_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placement_cell.publication')),
            ],
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement', models.CharField(default='', max_length=100)),
                ('achievement_type', models.CharField(choices=[('EDUCATIONAL', 'Educational'), ('OTHER', 'Other')], default='OTHER', max_length=20)),
                ('description', models.TextField(blank=True, default='', max_length=1000, null=True)),
                ('issuer', models.CharField(default='', max_length=200)),
                ('date_earned', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placement_cell.placementrecord')),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
            options={
                'unique_together': {('record_id', 'unique_id')},
            },
        ),
        migrations.CreateModel(
            name='PlacementStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invitation', models.CharField(choices=[('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected'), ('PENDING', 'Pending'), ('IGNORE', 'IGNORE')], default='PENDING', max_length=20)),
                ('placed', models.CharField(choices=[('NOT PLACED', 'Not Placed'), ('PLACED', 'Placed')], default='NOT PLACED', max_length=20)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('no_of_days', models.IntegerField(blank=True, default=10, null=True)),
                ('notify_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placement_cell.notifystudent')),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
            options={
                'unique_together': {('notify_id', 'unique_id')},
            },
        ),
        migrations.CreateModel(
            name='Has',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_rating', models.IntegerField(default=80)),
                ('skill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placement_cell.skill')),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
            options={
                'unique_together': {('skill_id', 'unique_id')},
            },
        ),
    ]
