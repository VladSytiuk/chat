# Generated by Django 3.2.7 on 2021-09-30 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_comment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='comments',
            field=models.ManyToManyField(blank=True, null=True, to='mainapp.Comment'),
        ),
    ]