from django.contrib import admin
#from .models import Book
#from .models import Lesson
##from .models import Category, Photo
from .models import Lesson, Textbook

#admin.site.register(Book)
#admin.site.register(Lesson)

#class CategoryAdmin(admin.ModelAdmin):
#    list_display = ('id', 'title')
#    list_display_links = ('id', 'title')

#class PhotoAdmin(admin.ModelAdmin):
#    list_display = ('id', 'title', 'user')
#    list_display_links = ('id', 'title')

#admin.site.register(Category, CategoryAdmin)
#admin.site.register(Photo, PhotoAdmin)

class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

#class StatusAdmin(admin.ModelAdmin):
#    list_display = ('id', 'title')
#    list_display_links = ('id', 'title')

#class DepartmentAdmin(admin.ModelAdmin):
#    list_display = ('id', 'title')
#    list_display_links = ('id', 'title')

#class SchoolyearAdmin(admin.ModelAdmin):
#    list_display = ('id', 'title')
#    list_display_links = ('id', 'title')

class TextbookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user')
    list_display_links = ('id', 'title')

admin.site.register(Lesson, LessonAdmin)
#admin.site.register(Status, StatusAdmin)
#admin.site.register(Department, DepartmentAdmin)
#admin.site.register(Schoolyear, SchoolyearAdmin)
admin.site.register(Textbook, TextbookAdmin)
