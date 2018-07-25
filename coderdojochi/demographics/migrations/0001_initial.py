# Generated by Django 2.0.6 on 2018-07-24 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ethnicity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ethnicity', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Ethnicity',
                'verbose_name_plural': 'Ethnicities',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=255)),
                ('referred_to_as', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], default='F', max_length=1)),
            ],
            options={
                'verbose_name': 'Gender',
                'verbose_name_plural': 'Genders',
            },
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Race',
                'verbose_name_plural': 'Races',
            },
        ),
        migrations.AddField(
            model_name='ethnicity',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demographics.Race'),
        ),
    ]
