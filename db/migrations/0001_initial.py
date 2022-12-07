# Generated by Django 4.1.3 on 2022-11-27 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('choose', models.BooleanField(default=False)),
            ],
        ),
    ]
