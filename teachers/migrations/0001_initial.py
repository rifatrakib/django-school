# Generated by Django 3.2.5 on 2021-07-26 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0005_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.customuser')),
                ('identity', models.CharField(max_length=50, unique=True)),
                ('started_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
