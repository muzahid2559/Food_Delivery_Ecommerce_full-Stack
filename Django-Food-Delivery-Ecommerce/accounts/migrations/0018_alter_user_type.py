# Generated by Django 4.1.4 on 2023-01-05 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('seller', 'seller'), ('deliver', 'deliver'), ('buyer', 'buyer')], max_length=10),
        ),
    ]
