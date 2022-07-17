from django.contrib import admin
from django.utils.html import format_html
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'thumbnail_preview')
    search_fields = ('title', 'category')
    list_filter = ('category',)
    readonly_fields = ('thumbnail_preview', 'image_preview')

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview
    def image_preview(self, obj):
        return obj.image_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "author":
            kwargs["queryset"] = Post.objects.filter()
        return super(PostAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    #raw_id_fields = ["author"]

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "tag":
            kwargs["queryset"] = Tag.objects.filter()
        return super(PostAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
    #raw_id_fields = ["tag"]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.filter()
        return super(PostAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    
    raw_id_fields = ["category", "author"]
    # autocomplete_fields = ("category", "tag", "author",)
    filter_horizontal = ("tag",)

    def thumbnail(self, obj):
        return format_html('<img src="{{ post.image.url }}" style="width: 130px; height: 100px"/>'.format(obj.thumbnail))

    thumbnail.short_description = 'thumbnail'

admin.site.register(Post, PostAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'username', 'mobile', 'is_staff')
    search_fields = ('first_name', 'email', 'username', 'mobile')
    list_filter = ('first_name',)

admin.site.register(User, UserAdmin)


class CategoryAdmin(admin.ModelAdmin):
    search_fields: ('category')

admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    search_fields: ('tag')

admin.site.register(Tag, TagAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display: ('post')

admin.site.register(Comment, CommentAdmin)
