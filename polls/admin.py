# coding:utf8
from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # 显示个别字段，作为列显示，即简要信息
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 增加filter过滤器
    list_filter = ['pub_date']
    # 增加搜索功能
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
