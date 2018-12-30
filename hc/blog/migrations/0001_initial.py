# Generated by Django 2.1.4 on 2018-12-30 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63)),
                ('slug', models.SlugField(max_length=63)),
                ('text', models.TextField()),
                ('pub_date', models.DateField()),
                ('startups', models.ManyToManyField(to='organizer.Startup')),
                ('tags', models.ManyToManyField(to='organizer.Tag')),
            ],
            options={
                'verbose_name': 'blog_post',
                'ordering': ['-pub_date', 'title'],
                'get_latest_by': 'pub_date',
            },
        ),
    ]
