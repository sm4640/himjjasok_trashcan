from django.contrib import admin

from .models import advice_him, advice_jja, advice_sok
# Register your models here.

@admin.register(advice_him)
class model_him(admin.ModelAdmin):
    list_display = ('id', 'content', )
    
@admin.register(advice_jja)
class model_jja(admin.ModelAdmin):
    list_display = ('id', 'content', )
    
@admin.register(advice_sok)
class model_sok(admin.ModelAdmin):
    list_display = ('id', 'content', )