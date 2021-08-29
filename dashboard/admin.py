from django.contrib import admin
from dashboard.models import LogHistory

@admin.register(LogHistory)
class LogHistoryAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'category', 'message')
    list_filter = ('category',)
