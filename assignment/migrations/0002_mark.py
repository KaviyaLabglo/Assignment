# Generated by Django 3.2.12 on 2022-10-03 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100, null=True)),
                ('mark', models.IntegerField()),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('stu_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assignment.student')),
            ],
        ),
    ]