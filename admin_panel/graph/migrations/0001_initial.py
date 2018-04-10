# Generated by Django 2.0.4 on 2018-04-10 13:21

from django.db import migrations, models
import graph.validate


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('func', models.CharField(help_text='allowed symbols: t, *, -, +, /, 0-9', max_length=100, validators=[graph.validate.validate_function], verbose_name='function')),
                ('interval', models.PositiveSmallIntegerField(help_text='the depth of the simulation period in days', verbose_name='depth')),
                ('dt', models.PositiveSmallIntegerField(help_text='step in hours', verbose_name='step')),
                ('graph', models.ImageField(null=True, upload_to='graphs')),
                ('error', models.TextField(blank=True, null=True, verbose_name='error')),
                ('handling_date', models.DateTimeField(null=True, verbose_name='handling date')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Graph',
                'verbose_name_plural': 'Graphs',
            },
        ),
    ]