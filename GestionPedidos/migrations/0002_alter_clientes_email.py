# Generated by Django 3.2.3 on 2021-05-24 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionPedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
