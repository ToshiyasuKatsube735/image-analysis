from django.contrib import admin
from .models import ai_analysis_log

# Register your models here.
@admin.register(ai_analysis_log)
class ai_analysis_logAdmin(admin.ModelAdmin):
    list_display = ('image_path', 'success', 'image_class', 'confidence')
    list_filter = ('success', 'image_class')
    search_fields = ('image_path',)
    ordering = ('image_path',)
