# Generated by Django 5.0.2 on 2024-02-15 12:36

import django.db.models.deletion
import django.utils.timezone
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Waste',
            fields=[
                ('waste_id', models.AutoField(primary_key=True, serialize=False)),
                ('waste_type', models.CharField(max_length=100)),
                ('waste_desc', models.CharField(max_length=500)),
                ('collection_price', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='CollectorProfile',
            fields=[
                ('collector_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehicle', models.CharField(max_length=200)),
                ('work_area', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('waste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collector_wastes', to='base.waste')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('collection_id', models.AutoField(primary_key=True, serialize=False)),
                ('collection_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('collector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collections_collected', to='base.collectorprofile')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.TextField(max_length=200)),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('rating_id', models.AutoField(primary_key=True, serialize=False)),
                ('rating_score', models.PositiveIntegerField()),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='base.collection')),
            ],
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.TextField(max_length=254)),
                ('number_of_bags', models.PositiveIntegerField()),
                ('request_status', models.CharField(max_length=100)),
                ('request_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('collection_price', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_requests', to='base.customerprofile')),
                ('waste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='base.waste')),
            ],
        ),
        migrations.AddField(
            model_name='collection',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collections_requested', to='base.requests'),
        ),
    ]
