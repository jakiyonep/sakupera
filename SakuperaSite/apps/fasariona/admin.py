from django.contrib import admin
from .models import *

"""
========== Dict ==========
"""

admin.site.register(Pos)
admin.site.register(Sentence)

class WordDescInline(admin.TabularInline):
    model = Description
    extra = 1
    readonly_fields = ['id', 'created_at', 'modified_at']

class WordAdmin(admin.ModelAdmin):
    inlines = [WordDescInline]

admin.site.register(Word, WordAdmin)

"""
========== Gwiki ==========
"""

admin.site.register(WikiNote)