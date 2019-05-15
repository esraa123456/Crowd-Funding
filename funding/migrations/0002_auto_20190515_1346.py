# Generated by Django 2.1 on 2019-05-15 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='detials',
        ),
        migrations.AddField(
            model_name='project',
            name='details',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]