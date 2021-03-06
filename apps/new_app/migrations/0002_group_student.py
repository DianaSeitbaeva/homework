# Generated by Django 3.0 on 2022-02-04 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(verbose_name='Возраст студента')),
                ('GPA', models.FloatField(verbose_name='Средний значение GPA')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='new_app.Account')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='new_app.Group')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
                'ordering': ('account', 'age', 'group', 'GPA'),
            },
        ),
    ]
