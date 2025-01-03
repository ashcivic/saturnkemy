# Generated by Django 5.1.3 on 2024-12-15 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContasPagar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('data_vencimento', models.DateField(verbose_name='Data de Vencimento')),
                ('pago', models.BooleanField(default=False, verbose_name='Pago?')),
            ],
        ),
        migrations.CreateModel(
            name='ContasReceber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('data_recebimento', models.DateField(verbose_name='Data de Recebimento')),
                ('recebido', models.BooleanField(default=False, verbose_name='Recebido?')),
            ],
        ),
        migrations.CreateModel(
            name='Entregas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entregador', models.CharField(max_length=255, verbose_name='Entregador')),
                ('custo', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Custo')),
                ('destino', models.CharField(max_length=255, verbose_name='Destino')),
                ('data_entrega', models.DateField(verbose_name='Data da Entrega')),
            ],
        ),
        migrations.CreateModel(
            name='Vendas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=255, verbose_name='Produto')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor Total')),
                ('data', models.DateField(verbose_name='Data da Venda')),
            ],
        ),
    ]
