# Generated by Django 5.1.1 on 2024-10-02 09:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Connection_Bank_Details',
        ),
        migrations.AddField(
            model_name='connection',
            name='c_GSTIN',
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='connection',
            name='cbd_account_no',
            field=models.IntegerField(default=674567453437564),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='connection',
            name='cbd_bank_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='connection',
            name='cbd_branch',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='connection',
            name='cbd_ifsc',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='connection',
            name='cbd_swift_code',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
