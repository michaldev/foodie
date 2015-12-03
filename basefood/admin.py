from django.contrib import admin
from basefood.models import \
    Category, CategoryMain, Product, Vitamin, \
    Preservative, Shop, Mineral, ShopLocal, \
    Ingredient, Producer


class Every(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ShopLocalAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('address', 'city',)}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', 'producer')}


admin.site.register(Category, Every)
admin.site.register(CategoryMain, Every)
admin.site.register(Product, ProductAdmin)
admin.site.register(Vitamin, Every)
admin.site.register(Preservative, Every)
admin.site.register(Mineral, Every)
admin.site.register(Shop, Every)
admin.site.register(ShopLocal, ShopLocalAdmin)
admin.site.register(Ingredient, Every)
admin.site.register(Producer, Every)
