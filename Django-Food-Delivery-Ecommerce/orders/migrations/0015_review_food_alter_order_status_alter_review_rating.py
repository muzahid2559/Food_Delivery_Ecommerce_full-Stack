# Generated by Django 4.1.4 on 2023-01-04 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_delete_review'),
        ('orders', '0014_alter_order_cart_alter_order_status_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='food',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.food'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('paid', 'Paid'), ('on_the_way', 'On The Way'), ('stolen', 'Stolen'), ('delivered', 'Delivered'), ('pending', 'Pending')], max_length=20),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('5', '5'), ('3', '3'), ('4', '4'), ('1', '1'), ('2', '2')], max_length=5),
        ),
    ]