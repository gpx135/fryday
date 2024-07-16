from django.contrib import admin
from .models import (
    FoodCategory, FoodCategoryTranslation, FoodItem, FoodItemTranslation,
    DietaryPreference, DietaryPreferenceTranslation, FoodItemDietaryInfo
)

@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(FoodCategoryTranslation)
class FoodCategoryTranslationAdmin(admin.ModelAdmin):
    list_display = ('category', 'language', 'name')
    search_fields = ('category__name', 'language__code', 'name')

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_available', 'price', 'created_at')
    search_fields = ('name', 'category__name', 'description')
    list_filter = ('category', 'is_available')

@admin.register(FoodItemTranslation)
class FoodItemTranslationAdmin(admin.ModelAdmin):
    list_display = ('food_item', 'language', 'name')
    search_fields = ('food_item__name', 'language__code', 'name')

@admin.register(DietaryPreference)
class DietaryPreferenceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(DietaryPreferenceTranslation)
class DietaryPreferenceTranslationAdmin(admin.ModelAdmin):
    list_display = ('dietary_preference', 'language', 'name')
    search_fields = ('dietary_preference__name', 'language__code', 'name')

@admin.register(FoodItemDietaryInfo)
class FoodItemDietaryInfoAdmin(admin.ModelAdmin):
    list_display = ('food_item', 'dietary_info')
    search_fields = ('food_item__name', 'dietary_info__name')