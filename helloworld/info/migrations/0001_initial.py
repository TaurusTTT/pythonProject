# Generated by Django 3.2.3 on 2021-05-21 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='helloworld',
            fields=[
                ('stu_id', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('stu_name', models.CharField(max_length=20)),
                ('stu_vacci', models.BooleanField()),
            ],
        ),
    ]
