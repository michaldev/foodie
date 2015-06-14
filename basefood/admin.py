from django.contrib import admin
from basefood.models import Category, CategoryMain, Product, Vitamin, Preservative, Shop, Mineral, Price

class Every(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class PriceInline(admin.TabularInline):
    model = Price
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = (PriceInline,)

admin.site.register(Category, Every)
admin.site.register(CategoryMain, Every)
admin.site.register(Product, ProductAdmin)
admin.site.register(Vitamin, Every)
admin.site.register(Preservative, Every)
admin.site.register(Mineral, Every)
admin.site.register(Shop, Every)
admin.site.register(Price)