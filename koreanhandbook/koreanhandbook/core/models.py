# Future imports
from __future__ import unicode_literals

# Django imports
from django.conf import settings
from django.db import models
from django.utils.timezone import now

class Tool(models.Model):
    full_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    icon_name = models.CharField(max_length=100, default='priority_high')
    def __str__(self):
       return 'Tool: ' + self.full_name

class Info(models.Model):
    full_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    num_colums =  models.IntegerField(default='2')
    column_1_name = models.CharField(max_length=100, default='col1')
    column_2_name =  models.CharField(max_length=100, default='col2')
    column_3_name =  models.CharField(max_length=100, default='col3')
    alphanumeric_order = models.BooleanField(default=False)
    numeric_first_col = models.BooleanField(default=False)
    icon_name = models.CharField(max_length=100, default='priority_high')
    description = models.TextField(default='')
    def __str__(self):
       return 'Info: ' + self.full_name

class Row_2(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    col_1 = models.CharField(max_length=255)
    col_2 = models.CharField(max_length=255)
    date_inserted = models.DateTimeField(default=now, blank=True)
    def __str__(self):
      return 'Row2' + self.info.short_name + ' : ' + str(self.id)

class Row_3(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    col_1 = models.CharField(max_length=255)
    col_2 = models.CharField(max_length=255)
    col_3 = models.CharField(max_length=255)
    date_inserted = models.DateTimeField(default=now, blank=True)
    def __str__(self):
      return 'Row3' + self.info.short_name + ' : ' + str(self.id)
