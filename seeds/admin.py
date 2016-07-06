from django.contrib import admin
from .models import ToDo

class SeedsAdmin(admin.ModelAdmin):
    list_display = ('name', 'assigned', 'status', 'creation_date')
    date_hierarchy = 'creation_date'
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(ToDo, SeedsAdmin)
