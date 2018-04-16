# Generated by Django 2.0.4 on 2018-04-11 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Backlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Backlog_Issues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_id', models.IntegerField()),
                ('priority', models.IntegerField()),
                ('backlog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='migrator_app.Backlog')),
            ],
        ),
        migrations.CreateModel(
            name='Source_Repo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='backlog',
            name='source_repo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='migrator_app.Source_Repo'),
        ),
    ]