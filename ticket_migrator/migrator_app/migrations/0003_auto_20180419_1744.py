# Generated by Django 2.0.4 on 2018-04-19 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('migrator_app', '0002_auto_20180411_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backlog',
            name='source_repo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='migrator_app.Source_Repo'),
        ),
    ]