# Generated by Django 3.1.5 on 2021-03-18 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=34)),
                ('seña', models.IntegerField(null=True)),
                ('decimales', models.DecimalField(decimal_places=2, max_digits=10)),
                ('vacunas', models.CharField(max_length=64)),
                ('días_nacido', models.IntegerField(null=True)),
            ],
        ),
    ]
