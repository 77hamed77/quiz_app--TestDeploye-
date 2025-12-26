from django.contrib import admin
from .models import Quiz, Question, Choice

# طريقة لعرض الخيارات داخل صفحة السؤال مباشرة (للسهولة)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4  # عدد الخيارات الافتراضي

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice) # لا نحتاج تسجيله منفصلاً لأنه سيظهر داخل السؤال