# Generated by Django 2.1.4 on 2018-12-10 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('test_id', models.AutoField(primary_key=True, serialize=False)),
                ('test_name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
