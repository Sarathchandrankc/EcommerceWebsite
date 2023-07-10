# Generated by Django 4.1.1 on 2023-07-02 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('composition', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('category', models.CharField(choices=[('CZ', 'Cheeze'), ('LS', 'Lassi'), ('GH', 'Ghee'), ('PN', 'Paneer'), ('CR', 'Curd'), ('IC', 'Ice-Creams'), ('MS', 'Milkshake'), ('ML', 'Milk')], max_length=2)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]