# Generated by Django 5.1.3 on 2024-12-03 04:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=14, unique=True)),
                ('nome', models.CharField(max_length=255)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orcamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('valor_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade_estoque', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pedido', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('aberto', 'Em Aberto'), ('comprado', 'Comprado'), ('recebido', 'Recebido'), ('cancelado', 'Cancelado'), ('recebido_parcial', 'Recebido Parcialmente')], default='aberto', max_length=20)),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True)),
                ('editado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pedidos_editados', to=settings.AUTH_USER_MODEL)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos_criados', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_pedida', models.PositiveIntegerField()),
                ('quantidade_recebida', models.PositiveIntegerField(default=0)),
                ('data_lancamento', models.DateTimeField(auto_now=True)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='drogaria.pedido')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drogaria.produto')),
            ],
        ),
        migrations.CreateModel(
            name='ItemOrcamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('valor_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('desconto', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('orcamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='drogaria.orcamento')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drogaria.produto')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma_pagamento', models.CharField(max_length=255)),
                ('desconto', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('entrega', models.JSONField(blank=True, null=True)),
                ('data_venda', models.DateTimeField(auto_now_add=True)),
                ('orcamento', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='drogaria.orcamento')),
            ],
        ),
    ]
