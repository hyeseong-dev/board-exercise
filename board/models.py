# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Album(models.Model):
    a_no = models.AutoField(primary_key=True)
    a_type = models.CharField(max_length=50)
    a_title = models.CharField(max_length=255)
    a_note = models.CharField(max_length=4096, blank=True, null=True)
    a_image = models.CharField(max_length=1024, blank=True, null=True)
    a_count = models.IntegerField()
    a_datetime = models.DateTimeField()
    a_usage = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'album'


class Board(models.Model):
    b_no = models.AutoField(db_column='b_no', primary_key=True)
    b_title = models.CharField(db_column='b_title', max_length=255)
    b_note = models.TextField(db_column='b_note', )
    b_writer = models.CharField(db_column='b_writer', max_length=50)
    parent_no = models.IntegerField(db_column='parent_no', default=0)
    b_count = models.IntegerField(db_column='b_count', default=0)
    b_created_date = models.DateTimeField(db_column='b_created_date', auto_now_add=True)
    b_updated_date = models.DateTimeField(db_column='b_updated_date', auto_now=True)
    usage_flag = models.CharField(db_column='usage_flag', max_length=11, default='1')

    class Meta:
        managed = True
        db_table = 'board'

    def __str__(self):
        return "제목 : " + self.b_title + ", 작성자 : " + self.b_writer


class Board2(models.Model):
    b_no = models.AutoField(primary_key=True)
    b_title = models.CharField(max_length=255)
    b_note = models.CharField(max_length=4096, blank=True, null=True)
    parent_no = models.IntegerField(blank=True, null=True)
    b_writer = models.CharField(max_length=50, blank=True, null=True)
    b_count = models.IntegerField(blank=True, null=True)
    b_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'board2'


class SalesPredict(models.Model):
    yyyymm = models.CharField(max_length=20, blank=True, null=True)
    sales_amt = models.IntegerField(blank=True, null=True)
    sales_predict = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_predict'
