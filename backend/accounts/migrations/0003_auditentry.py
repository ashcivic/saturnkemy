# Generated by Django 4.1.3 on 2023-01-15 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('action', models.CharField(max_length=64)),
                ('ip', models.GenericIPAddressField(null=True)),
                ('email', models.CharField(max_length=256, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
