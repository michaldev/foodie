from django.contrib import admin
from basefood.models import Category, CategoryMain, Product, Vitamin, Preservative, Shop, Mineral

class Every(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, Every)
admin.site.register(CategoryMain, Every)
admin.site.register(Product, Every)
admin.site.register(Vitamin, Every)
admin.site.register(Preservative, Every)
admin.site.register(Mineral, Every)
admin.site.register(Shop, Every)