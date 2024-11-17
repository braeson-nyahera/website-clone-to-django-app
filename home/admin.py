from django.contrib import admin
from .models import Team, Testimonial, Blog

# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name','position']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=['title','author']