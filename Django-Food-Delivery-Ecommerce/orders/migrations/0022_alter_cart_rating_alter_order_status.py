# Generated by Django 4.1.4 on 2023-01-05 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_alter_cart_rating_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='rating',
            field=models.CharField(blank=True, choices=[('5', '5'), ('2', '2'), ('3', '3'), ('4', '4'), ('1', '1')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('delivered', 'Delivered'), ('stolen', 'Stolen'), ('on_the_way', 'On The Way'), ('paid', 'Paid')], max_length=20),
        ),
    ]
