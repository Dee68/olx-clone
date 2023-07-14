from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from .models import Category, Product, ProductImage


# class CustomMPTTModelAdmin(MPTTModelAdmin):
#     mptt_level_indent = 20


admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
    prepopulated_fields = {'slug': ('title',)}
    )


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 10


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'seller', 'location', 'category', 'image_tag']
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]


admin.site.register(Product, ProductAdmin)
