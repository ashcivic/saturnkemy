# Generated by Django 5.1.3 on 2024-12-20 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0002_column_card'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Column',
            new_name='KanbanColumn',
        ),
    ]
