# Generated by Django 2.1b1 on 2018-07-08 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SHOP',
            fields=[
                ('shop_id', models.AutoField(default=False, primary_key=True, serialize=False, unique=True)),
                ('shop_name', models.CharField(default=False, max_length=256)),
                ('shop_address', models.CharField(blank=True, max_length=256, null=True)),
                ('shop_longitude', models.CharField(blank=True, max_length=256, null=True)),
                ('shop_latitude', models.CharField(blank=True, max_length=1000, null=True)),
                ('shop_NTN', models.IntegerField(blank=True, null=True)),
                ('shop_type', models.CharField(max_length=1000)),
                ('shop_description', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='SHOPtab',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='cdesc',
            new_name='category_description',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='discount',
            new_name='category_discount',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='promotion',
            new_name='category_promotion',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='catid',
            new_name='cat_id',
        ),
        migrations.RenameField(
            model_name='subcat',
            old_name='desc',
            new_name='subcategory_description',
        ),
        migrations.RenameField(
            model_name='subcat',
            old_name='discount',
            new_name='subcategory_discount',
        ),
        migrations.RenameField(
            model_name='subcat',
            old_name='promotion',
            new_name='subcategory_promotion',
        ),
        migrations.RemoveField(
            model_name='category',
            name='cid',
        ),
        migrations.RemoveField(
            model_name='category',
            name='cname',
        ),
        migrations.RemoveField(
            model_name='category',
            name='id',
        ),
        migrations.RemoveField(
            model_name='item',
            name='id',
        ),
        migrations.RemoveField(
            model_name='item',
            name='itemid',
        ),
        migrations.RemoveField(
            model_name='item',
            name='itemname',
        ),
        migrations.RemoveField(
            model_name='item',
            name='subcatid',
        ),
        migrations.RemoveField(
            model_name='subcat',
            name='id',
        ),
        migrations.RemoveField(
            model_name='subcat',
            name='name',
        ),
        migrations.RemoveField(
            model_name='subcat',
            name='subcatid',
        ),
        migrations.AddField(
            model_name='category',
            name='category_id',
            field=models.AutoField(default=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name',
            field=models.CharField(default=False, max_length=256),
        ),
        migrations.AddField(
            model_name='item',
            name='item_PPU',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='item_description',
            field=models.CharField(default=False, max_length=256, unique=True),
        ),
        migrations.AddField(
            model_name='item',
            name='item_discount',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='item_id',
            field=models.AutoField(default=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.FileField(default=False, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='item_name',
            field=models.CharField(default=False, max_length=256),
        ),
        migrations.AddField(
            model_name='item',
            name='item_price',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='item_promotion',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='item_quantity',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='item_rating',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='item_tag',
            field=models.CharField(default=False, max_length=256),
        ),
        migrations.AddField(
            model_name='item',
            name='item_unit',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='subcat_id',
            field=models.IntegerField(default=False, unique=True),
        ),
        migrations.AddField(
            model_name='subcat',
            name='subcategory_id',
            field=models.AutoField(default=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='subcat',
            name='subcategory_name',
            field=models.CharField(default=False, max_length=256),
        ),
    ]
