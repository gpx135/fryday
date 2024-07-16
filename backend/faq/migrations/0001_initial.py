# Generated by Django 4.2.1 on 2024-07-15 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('localization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('answer', models.TextField(blank=True)),
                ('category', models.CharField(blank=True, max_length=100)),
                ('order_index', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
                'ordering': ['order_index', 'id'],
            },
        ),
        migrations.CreateModel(
            name='FAQTranslation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('answer', models.TextField(blank=True)),
                ('faq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faq.faq')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localization.language')),
            ],
            options={
                'verbose_name': 'FAQ Translation',
                'verbose_name_plural': 'FAQ Translations',
                'unique_together': {('faq', 'language')},
            },
        ),
    ]
