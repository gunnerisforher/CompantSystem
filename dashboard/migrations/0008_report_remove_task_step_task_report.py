# Generated by Django 4.1.2 on 2022-11-02 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_department_colleagues_department_tasks_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='step',
        ),
        migrations.AddField(
            model_name='task',
            name='report',
            field=models.ManyToManyField(blank=True, to='dashboard.report'),
        ),
    ]
