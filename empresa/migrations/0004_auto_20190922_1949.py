# Generated by Django 2.0 on 2019-09-23 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_auto_20190922_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='cnpj_cpf',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='razao_social',
            field=models.CharField(max_length=66, unique=True),
        ),
    ]
