# Generated by Django 4.2.1 on 2024-07-15 05:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuffetPricing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('day_of_week', models.IntegerField(choices=[(0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')])),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'verbose_name': 'Buffet Pricing',
                'verbose_name_plural': 'Buffet Pricing',
            },
        ),
        migrations.CreateModel(
            name='SpecialGroupPricing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('buffet_pricing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricing.buffetpricing')),
                ('user_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.usergroup')),
            ],
            options={
                'verbose_name': 'Special Group Pricing',
                'verbose_name_plural': 'Special Group Pricing',
            },
        ),
        migrations.AddConstraint(
            model_name='buffetpricing',
            constraint=models.CheckConstraint(check=models.Q(('start_time__lt', models.F('end_time'))), name='start_time_before_end_time'),
        ),
        migrations.AlterUniqueTogether(
            name='specialgrouppricing',
            unique_together={('user_group', 'buffet_pricing')},
        ),
    ]
