from django.contrib import admin
from .models import Home, TitleSection, Section, Statistics, Hystories
# Register your models here.



@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ["title", "description",]
    

@admin.register(TitleSection)
class TitleSectionAdmin(admin.ModelAdmin):
    list_display = ["home","title", ]
    
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ["titleSection", 'title', 'content']
    
