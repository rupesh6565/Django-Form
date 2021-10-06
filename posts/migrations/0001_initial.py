# Generated by Django 3.1 on 2021-10-01 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='Annonymous', max_length=14, verbose_name='Name')),
                ('body', models.CharField(blank=True, db_index=True, max_length=140, null=True, verbose_name='Body')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created DateTime')),
            ],
            options={
                'db_table': 'posts',
            },
        ),
    ]
