# Generated by Django 5.1.3 on 2024-12-13 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('To Do', 'To Do'), ('In Progress', 'In Progress'), ('Done', 'Done')], max_length=50)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_limite', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
