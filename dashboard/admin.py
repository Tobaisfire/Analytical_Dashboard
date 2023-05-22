from django.contrib import admin
from .models import UploadedFile
# Register your models here.
@admin.register(UploadedFile)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('file',)
    # search_fields = ('field1', 'field2')
    # list_filter = ('field3',)