# Generated by Django 2.0.7 on 2018-12-04 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_auto_20181204_1523'),
        ('bouncer', '0005_auto_20181204_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cards_seen',
            field=models.ManyToManyField(to='content.Card'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='f955766f-c4b6-422c-9363-0f44beb4747a', editable=False, max_length=36, primary_key=True, serialize=False, unique=True),
        ),
    ]
