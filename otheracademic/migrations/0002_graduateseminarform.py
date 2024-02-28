# Generated by Django 3.1.5 on 2024-02-20 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0005_auto_20240220_0718'),
        ('otheracademic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraduateSeminarForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=100)),
                ('date_of_seminar', models.DateField()),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
            options={
                'db_table': 'GraduateSeminarForm',
            },
        ),
    ]