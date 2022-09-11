# Generated by Django 4.1.1 on 2022-09-11 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_andao_atakalo', '0006_alter_owner_id_alter_picture_id_alter_toy_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='path',
        ),
        migrations.AddField(
            model_name='picture',
            name='image_url',
            field=models.ImageField(default='', upload_to='uploads'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picture',
            name='toy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='api_andao_atakalo.toy'),
        ),
        migrations.AlterField(
            model_name='toy',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toys', to='api_andao_atakalo.owner'),
        ),
    ]
