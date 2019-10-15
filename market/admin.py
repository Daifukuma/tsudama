from django.contrib import admin
from .models import Book
from .models import Lesson
from .models import Category, Photo

admin.site.register(Book)
admin.site.register(Lesson)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user')
    list_display_links = ('id', 'title')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)
