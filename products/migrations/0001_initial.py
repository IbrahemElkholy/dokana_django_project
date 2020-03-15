# Generated by Django 3.0.3 on 2020-03-14 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryID', models.IntegerField(primary_key=True, serialize=False)),
                ('categoryName', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('productID', models.IntegerField(primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=200)),
                ('productDetails', models.CharField(max_length=500)),
                ('productImg', models.ImageField(blank=True, null=True, upload_to='')),
                ('productModel', models.CharField(max_length=200)),
                ('productAverageRating', models.IntegerField(default=0)),
                ('productCount', models.IntegerField(default=0)),
                ('productPrice', models.IntegerField(default=0)),
                ('categoryID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=1000)),
                ('productID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Products')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.User')),
            ],
            options={
                'unique_together': {('productID', 'userID')},
            },
        ),
    ]
