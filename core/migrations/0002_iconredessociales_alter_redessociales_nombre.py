# Generated by Django 5.0.3 on 2024-03-26 22:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IconRedesSociales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='red social')),
                ('icon', models.ImageField(upload_to='icons_redes_sociales')),
            ],
        ),
        migrations.AlterField(
            model_name='redessociales',
            name='nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.iconredessociales', verbose_name='red social'),
        ),
    ]