# Generated by Django 3.2.8 on 2021-10-20 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_postpage_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=255)),
                ('ToSLink', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Footer Text',
            },
        ),
    ]