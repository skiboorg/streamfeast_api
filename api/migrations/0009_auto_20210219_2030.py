# Generated by Django 3.1.5 on 2021-02-19 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210216_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='howto',
            name='icon',
            field=models.ImageField(null=True, upload_to='icons/', verbose_name='Иконка'),
        ),
        migrations.AlterField(
            model_name='howto',
            name='question',
            field=models.TextField(null=True, verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='links', to='api.streamer', verbose_name='Стример'),
        ),
    ]