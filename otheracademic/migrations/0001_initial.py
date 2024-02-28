# Generated by Django 3.1.5 on 2024-02-20 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('globals', '0004_auto_20240219_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveFormTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('date_of_application', models.DateField()),
                ('upload_file', models.FileField(blank=True, upload_to='')),
                ('address', models.CharField(max_length=100)),
                ('purpose', models.TextField()),
                ('leave_type', models.CharField(choices=[('Casual', 'Casual'), ('Medical', 'Medical')], max_length=20)),
                ('approved', models.BooleanField()),
                ('rejected', models.BooleanField()),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
            options={
                'db_table': 'LeaveFormTable',
            },
        ),
    ]