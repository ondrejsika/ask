from django.contrib import admin

from ask.models import Poll, Question, Answer, UserAnswer


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'poll',
        'question',
        'allow_user_answer',
    )
    list_display_links = list_display
    list_filter = list_display


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'poll',
        'question',
        'answer',
    )
    list_display_links = list_display
    list_filter = list_display


class UserAnswerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'poll',
        'question',
        'answer',
    )
    list_display_links = list_display
    list_filter = list_display


admin.site.register(Poll)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(UserAnswer, UserAnswerAdmin)
