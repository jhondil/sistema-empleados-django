# Generated by Django 3.1.7 on 2021-05-17 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_empleado_habilidades'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
        migrations.AlterField(
            model_name='empleado',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
    ]
