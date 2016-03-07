from django.contrib import admin

# Register your models here.
from blog.models import Blog, Category

class BlogAdnim(admin.ModelAdmin):
    exclude =['posted']
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog)
admin.site.register(Category);
