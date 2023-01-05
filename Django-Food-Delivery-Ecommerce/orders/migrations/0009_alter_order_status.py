# Generated by Django 4.1.4 on 2023-01-03 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('paid', 'Paid'), ('delivered', 'Delivered'), ('on_the_way', 'On The Way'), ('stolen', 'Stolen'), ('pending', 'Pending')], max_length=20),
        ),
    ]
