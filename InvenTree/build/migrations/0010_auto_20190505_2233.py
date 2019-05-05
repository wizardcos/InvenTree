# Generated by Django 2.2 on 2019-05-05 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0009_build_completed_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='part',
            field=models.ForeignKey(limit_choices_to={'active': True, 'buildable': True}, on_delete=django.db.models.deletion.CASCADE, related_name='builds', to='part.Part'),
        ),
    ]
