# Generated by Django 5.1.3 on 2024-12-17 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sngpc', '0003_produto_delete_establishmentconfig_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfiguracaoSngpc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ambiente', models.CharField(choices=[('homologacao', 'Homologação'), ('producao', 'Produção')], default='homologacao', max_length=20)),
            ],
        ),
    ]