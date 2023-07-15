# Generated by Django 4.1.7 on 2023-05-17 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_collection_user_alter_subscription_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.userprofile'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.userprofile'),
        ),
    ]
