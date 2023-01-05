# Generated by Django 4.1.4 on 2023-01-03 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('stolen', 'Stolen'), ('pending', 'Pending'), ('delivered', 'Delivered'), ('on_the_way', 'On The Way'), ('paid', 'Paid')], max_length=20),
        ),
    ]
