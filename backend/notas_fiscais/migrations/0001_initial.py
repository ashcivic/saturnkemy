# Generated by Django 5.1.3 on 2024-12-10 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificado', models.FileField(upload_to='certificados/')),
                ('senha', models.CharField(max_length=100)),
                ('ambiente', models.CharField(choices=[('homologacao', 'Homologação'), ('producao', 'Produção')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='NFE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido_id', models.CharField(max_length=100)),
                ('data_emissao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NFSe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formula_id', models.CharField(max_length=100)),
                ('data_emissao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
