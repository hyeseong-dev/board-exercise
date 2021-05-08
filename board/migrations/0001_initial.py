# Generated by Django 3.2.2 on 2021-05-08 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('a_no', models.AutoField(primary_key=True, serialize=False)),
                ('a_type', models.CharField(max_length=50)),
                ('a_title', models.CharField(max_length=255)),
                ('a_note', models.CharField(blank=True, max_length=4096, null=True)),
                ('a_image', models.CharField(blank=True, max_length=1024, null=True)),
                ('a_count', models.IntegerField()),
                ('a_datetime', models.DateTimeField()),
                ('a_usage', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'album',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Board2',
            fields=[
                ('b_no', models.AutoField(primary_key=True, serialize=False)),
                ('b_title', models.CharField(max_length=255)),
                ('b_note', models.CharField(blank=True, max_length=4096, null=True)),
                ('parent_no', models.IntegerField(blank=True, null=True)),
                ('b_writer', models.CharField(blank=True, max_length=50, null=True)),
                ('b_count', models.IntegerField(blank=True, null=True)),
                ('b_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'board2',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SalesPredict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yyyymm', models.CharField(blank=True, max_length=20, null=True)),
                ('sales_amt', models.IntegerField(blank=True, null=True)),
                ('sales_predict', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sales_predict',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('b_no', models.AutoField(db_column='b_no', primary_key=True, serialize=False)),
                ('b_title', models.CharField(db_column='b_title', max_length=255)),
                ('b_note', models.TextField(db_column='b_note')),
                ('b_writer', models.CharField(db_column='b_writer', max_length=50)),
                ('parent_no', models.IntegerField(db_column='parent_no', default=0)),
                ('b_count', models.IntegerField(db_column='b_count', default=0)),
                ('b_date', models.DateTimeField(db_column='b_date')),
                ('usage_flag', models.CharField(db_column='usage_flag', default='1', max_length=11)),
            ],
            options={
                'db_table': 'board',
                'managed': True,
            },
        ),
    ]
