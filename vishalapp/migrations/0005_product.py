# Generated by Django 4.1.4 on 2022-12-27 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vishalapp', '0004_rename_firstlogin_user_fristlogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Kid', 'kID')], max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.PositiveSmallIntegerField()),
                ('product_desc', models.TextField()),
                ('product_pic', models.ImageField(upload_to='product_pic/')),
                ('product_size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('2XL', '2XL')], max_length=100)),
                ('product_seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vishalapp.user')),
            ],
        ),
    ]
