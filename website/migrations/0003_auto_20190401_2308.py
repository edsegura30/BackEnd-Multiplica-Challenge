# Generated by Django 2.1.8 on 2019-04-02 05:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20190401_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='id',
        ),
        migrations.AddField(
            model_name='event',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website.EventType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='reporter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website.Reporter'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='uuid',
            field=models.UUIDField(primary_key=True, serialize=False, verbose_name='uuid'),
        ),
    ]