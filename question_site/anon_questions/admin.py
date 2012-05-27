from anon_questions.models import Question, Answer
from django.contrib import admin
class AnswerInline(admin.StackedInline):
    model = Question
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['question']}),
        ("Date information",    {'fields': ['ask_date'], 'classes': ['collapse']})
    ]
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
