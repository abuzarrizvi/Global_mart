# Generated by Django 2.1b1 on 2018-07-08 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20180708_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='CAT_PROMOTION',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cat_Promo_name', models.CharField(blank=True, max_length=256, null=True)),
                ('Cat_Promo_description', models.CharField(blank=True, max_length=1000, null=True)),
                ('Cat_Promo_start_date', models.DateTimeField()),
                ('Cat_Promo_end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ITEM_PROMOTION',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Promotion_name', models.CharField(blank=True, max_length=256, null=True)),
                ('Promotion_description', models.CharField(blank=True, max_length=1000, null=True)),
                ('Promotion_start_date', models.DateTimeField()),
                ('Promotion_end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ITEM_RATING',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SUBCAT_PROMOTION',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subcat_Promo_name', models.CharField(blank=True, max_length=256, null=True)),
                ('Subcat_Promo_description', models.CharField(blank=True, max_length=1000, null=True)),
                ('Subcat_Promo_start_date', models.DateTimeField()),
                ('Subcat_Promo_end_date', models.DateTimeField()),
            ],
        ),
        migrations.RenameField(
            model_name='item',
            old_name='item_rating',
            new_name='item_avg_rating',
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_promotion',
        ),
        migrations.AlterField(
            model_name='category',
            name='category_description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_promotion',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_latitude',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_type',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='subcat',
            name='subcategory_description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='subcat_promotion',
            name='Subcat_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.ITEM'),
        ),
        migrations.AddField(
            model_name='item_rating',
            name='Item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.ITEM'),
        ),
        migrations.AddField(
            model_name='item_promotion',
            name='Item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.ITEM'),
        ),
        migrations.AddField(
            model_name='cat_promotion',
            name='Cat_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.ITEM'),
        ),
    ]
