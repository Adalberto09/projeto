# Generated by Django 4.2.5 on 2023-09-23 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=300)),
                ('idade', models.IntegerField()),
                ('cpf', models.TextField(default='00000000000', max_length=11)),
            ],
        ),
    ]
