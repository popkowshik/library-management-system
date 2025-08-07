from django.contrib import admin
from .models import Review
# Register your models here.
@admin.register(Review)
class CastAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Review._meta.fields]
