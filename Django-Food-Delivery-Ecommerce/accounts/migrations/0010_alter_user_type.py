# Generated by Django 4.1.4 on 2023-01-04 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('deliver', 'deliver'), ('seller', 'seller'), ('buyer', 'buyer')], max_length=10),
        ),
    ]