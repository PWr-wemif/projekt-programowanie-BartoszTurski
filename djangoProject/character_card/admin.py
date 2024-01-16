from django.contrib import admin
from .models import Character
# Register your models here.
@admin.register(Character)
class PostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Character._meta.get_fields()]
