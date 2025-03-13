# Generated by Django 5.1.7 on 2025-03-13 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='nationality',
            field=models.CharField(blank=True, choices=[('USA', 'Estados Unidos'), ('Brazil', 'Brasil'), ('Portugal', 'Portugal'), ('Germany', 'Alemanha'), ('France', 'França'), ('Italy', 'Italia'), ('Spain', 'Espanha'), ('England', 'Inglaterra'), ('Mexico', 'Mexico'), ('Chile', 'Chile'), ('Colombia', 'Colombia'), ('Argentina', 'Argentina'), ('Peru', 'Peru'), ('Bolivia', 'Bolivia')], max_length=50, null=True),
        ),
    ]
