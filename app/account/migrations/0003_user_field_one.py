# Generated by Django 4.0.2 on 2022-06-29 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_user_is_customer_remove_user_is_employee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='field_one',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
