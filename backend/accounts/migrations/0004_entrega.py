# Generated by Django 5.1.3 on 2024-11-30 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auditentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('responsavel', models.CharField(max_length=100)),
                ('data_entrega', models.DateTimeField()),
            ],
        ),
    ]
