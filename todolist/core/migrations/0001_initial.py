# Generated by Django 4.2 on 2023-05-02 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='modelLista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarefa', models.CharField(max_length=70, verbose_name='tarefa')),
                ('dia', models.IntegerField(verbose_name='dia')),
                ('mes', models.IntegerField(verbose_name='mes')),
                ('ano', models.IntegerField(verbose_name='ano')),
            ],
        ),
    ]
