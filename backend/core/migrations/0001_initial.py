# Generated by Django 4.2.1 on 2024-07-15 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('day_of_week', models.IntegerField(choices=[(0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')])),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('is_closed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Opening Hours',
                'verbose_name_plural': 'Opening Hours',
            },
        ),
        migrations.CreateModel(
            name='SpecialClosure',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(unique=True)),
                ('reason', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Special Closure',
                'verbose_name_plural': 'Special Closures',
            },
        ),
        migrations.AddConstraint(
            model_name='openinghours',
            constraint=models.CheckConstraint(check=models.Q(('open_time__lt', models.F('close_time'))), name='open_time_before_close_time'),
        ),
    ]