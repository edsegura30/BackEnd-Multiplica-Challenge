# Generated by Django 2.1.8 on 2019-04-02 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(verbose_name='uuid')),
                ('name', models.CharField(max_length=240)),
            ],
        ),
    ]
