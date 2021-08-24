from django.contrib import admin
from .models import Question

# Register your models here.

# Model 등록
# admin.site.register(Question)

# Model 검색 (subject으로 검색)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)