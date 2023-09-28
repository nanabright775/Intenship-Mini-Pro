# Generated by Django 3.2 on 2023-09-27 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('log', '0006_alter_program_abb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.program')),
            ],
        ),
    ]