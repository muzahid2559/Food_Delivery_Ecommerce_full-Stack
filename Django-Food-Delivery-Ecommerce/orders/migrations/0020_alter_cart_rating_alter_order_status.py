# Generated by Django 4.1.4 on 2023-01-05 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_alter_cart_rating_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='rating',
            field=models.CharField(blank=True, choices=[('4', '4'), ('3', '3'), ('1', '1'), ('2', '2'), ('5', '5')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('delivered', 'Delivered'), ('on_the_way', 'On The Way'), ('stolen', 'Stolen'), ('pending', 'Pending'), ('paid', 'Paid')], max_length=20),
        ),
    ]
