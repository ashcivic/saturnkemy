# Generated by Django 5.1.3 on 2024-12-13 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('arquivo', models.FileField(upload_to='materiais/')),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('conteudo', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('ativa', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Promocao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('desconto_percentual', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('ativa', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=255)),
                ('cliente', models.CharField(max_length=255)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_venda', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('concluida', 'Concluída'), ('cancelada', 'Cancelada')], default='concluida', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='KitProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('desconto_percentual', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('produtos', models.ManyToManyField(to='ecommerce.venda')),
            ],
        ),
    ]
