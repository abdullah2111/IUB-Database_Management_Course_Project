# Generated by Django 4.2.7 on 2023-12-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testserver', '0003_alter_testproduct_prod_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testproduct',
            name='prod_ID',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
