# Generated by Django 2.0 on 2019-09-23 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0004_auto_20190922_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='cnpj_cpf',
            field=models.CharField(max_length=19),
        ),
    ]
