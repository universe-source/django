# coding:utf8
from __future__ import unicode_literals
import datetime

from django.utils import timezone
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return '{}'.format(self.question_text)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    # 增加属性描述
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently'

    class Meta(object):
        db_table = 'question'


class Choice(models.Model):
    """投票应用"""
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.choice_text)

    class Meta(object):
        db_table = 'choice'
