# Generated by Django 3.2.19 on 2023-07-03 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20230703_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmarks',
            name='marks',
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='studentmarks',
            unique_together={('student', 'subject')},
        ),
    ]
