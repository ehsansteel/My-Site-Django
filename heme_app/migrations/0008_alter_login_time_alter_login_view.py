# Generated by Django 4.0.5 on 2022-06-07 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heme_app', '0007_alter_login_body_alter_login_email_alter_login_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='time',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='view',
            field=models.DateTimeField(null=True),
        ),
    ]
