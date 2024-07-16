# Generated by Django 3.1.5 on 2024-07-16 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('programme_curriculum', '0001_initial'),
        ('globals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('description', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'Calendar',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=600)),
                ('course_details', models.TextField(max_length=500)),
            ],
            options={
                'db_table': 'Course',
            },
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('curriculum_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_code', models.CharField(max_length=20)),
                ('credits', models.IntegerField()),
                ('course_type', models.CharField(choices=[('Professional Core', 'Professional Core'), ('Professional Elective', 'Professional Elective'), ('Professional Lab', 'Professional Lab'), ('Engineering Science', 'Engineering Science'), ('Natural Science', 'Natural Science'), ('Humanities', 'Humanities'), ('Design', 'Design'), ('Manufacturing', 'Manufacturing'), ('Management Science', 'Management Science')], max_length=25)),
                ('programme', models.CharField(choices=[('B.Tech', 'B.Tech'), ('B.Des', 'B.Des'), ('M.Tech', 'M.Tech'), ('M.Des', 'M.Des'), ('PhD', 'PhD')], max_length=10)),
                ('branch', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('ME', 'ME'), ('DESIGN', 'DESIGN'), ('Common', 'Common')], default='Common', max_length=10)),
                ('batch', models.IntegerField()),
                ('sem', models.IntegerField()),
                ('optional', models.BooleanField(default=False)),
                ('floated', models.BooleanField(default=False)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.course')),
            ],
            options={
                'db_table': 'Curriculum',
                'unique_together': {('course_code', 'batch', 'programme')},
            },
        ),
        migrations.CreateModel(
            name='Curriculum_Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chief_inst', models.BooleanField(default=False)),
                ('curriculum_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.curriculum')),
                ('instructor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
            options={
                'db_table': 'Curriculum_Instructor',
                'unique_together': {('curriculum_id', 'instructor_id')},
            },
        ),
        migrations.CreateModel(
            name='Exam_timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_date', models.DateField(auto_now_add=True)),
                ('exam_time_table', models.FileField(upload_to='Administrator/academic_information/')),
                ('batch', models.IntegerField(default='2016')),
                ('programme', models.CharField(choices=[('B.Tech', 'B.Tech'), ('B.Des', 'B.Des'), ('M.Tech', 'M.Tech'), ('M.Des', 'M.Des'), ('PhD', 'PhD')], max_length=10)),
            ],
            options={
                'db_table': 'Exam_Timetable',
            },
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holiday_date', models.DateField()),
                ('holiday_name', models.CharField(max_length=40)),
                ('holiday_type', models.CharField(choices=[('restricted', 'restricted'), ('closed', 'closed'), ('vacation', 'vacation')], default='restricted', max_length=30)),
            ],
            options={
                'db_table': 'Holiday',
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=20)),
                ('agenda', models.TextField()),
                ('minutes_file', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'Meeting',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='globals.extrainfo')),
                ('programme', models.CharField(choices=[('B.Tech', 'B.Tech'), ('B.Des', 'B.Des'), ('M.Tech', 'M.Tech'), ('M.Des', 'M.Des'), ('PhD', 'PhD')], max_length=10)),
                ('batch', models.IntegerField(default=2016)),
                ('cpi', models.FloatField(default=0)),
                ('category', models.CharField(choices=[('GEN', 'General'), ('SC', 'Scheduled Castes'), ('ST', 'Scheduled Tribes'), ('OBC', 'Other Backward Classes')], max_length=10)),
                ('father_name', models.CharField(default='', max_length=40, null=True)),
                ('mother_name', models.CharField(default='', max_length=40, null=True)),
                ('hall_no', models.IntegerField(default=0)),
                ('room_no', models.CharField(blank=True, max_length=10, null=True)),
                ('specialization', models.CharField(choices=[('Power and Control', 'Power and Control'), ('Microwave and Communication Engineering', 'Microwave and Communication Engineering'), ('Micro-nano Electronics', 'Micro-nano Electronics'), ('CAD/CAM', 'CAD/CAM'), ('Design', 'Design'), ('Manufacturing', 'Manufacturing'), ('CSE', 'CSE'), ('Mechatronics', 'Mechatronics'), ('MDes', 'MDes'), ('None', 'None')], default='', max_length=40, null=True)),
                ('curr_semester_no', models.IntegerField(default=1)),
                ('batch_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='programme_curriculum.batch')),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('time_table', models.FileField(upload_to='Administrator/academic_information/')),
                ('batch', models.IntegerField(default='2016')),
                ('programme', models.CharField(choices=[('B.Tech', 'B.Tech'), ('B.Des', 'B.Des'), ('M.Tech', 'M.Tech'), ('M.Des', 'M.Des'), ('PhD', 'PhD')], max_length=10)),
                ('branch', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('ME', 'ME'), ('DESIGN', 'DESIGN'), ('Common', 'Common')], default='Common', max_length=10)),
            ],
            options={
                'db_table': 'Timetable',
            },
        ),
        migrations.CreateModel(
            name='Student_attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('present', models.BooleanField(default=False)),
                ('instructor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.curriculum_instructor')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
            options={
                'db_table': 'Student_attendance',
            },
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=4)),
                ('verify', models.BooleanField(default=False)),
                ('curriculum_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.curriculum')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
            options={
                'db_table': 'Grades',
            },
        ),
        migrations.CreateModel(
            name='Spi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.IntegerField()),
                ('spi', models.FloatField(default=0)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
            options={
                'db_table': 'Spi',
                'unique_together': {('student_id', 'sem')},
            },
        ),
    ]
