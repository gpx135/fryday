from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
from django.utils.translation import gettext_lazy as _



class FoodCategory(models.Model):
    """Stores food categories."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [GinIndex(fields=['search_vector'])]
        verbose_name = _("Food Category")
        verbose_name_plural = _("Food Categories")

    def __str__(self):
        return self.name

class FoodCategoryTranslation(models.Model):
    """Stores translations for food categories."""
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    language = models.ForeignKey('localization.Language', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ('category', 'language')
        verbose_name = _("Food Category Translation")
        verbose_name_plural = _("Food Category Translations")

    def __str__(self):
        return f"{self.category.name} - {self.language.code}"

class FoodItem(models.Model):
    """Stores information about food items."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    is_available = models.BooleanField(default=True)
    is_in_buffet = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    ingredients = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    additional_info = models.JSONField(default=dict, blank=True)
    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['is_available']),
            GinIndex(fields=['search_vector']),
            GinIndex(fields=['additional_info']),
        ]
        verbose_name = _("Food Item")
        verbose_name_plural = _("Food Items")

    def __str__(self):
        return self.name

class FoodItemTranslation(models.Model):
    """Stores translations for food items."""
    id = models.AutoField(primary_key=True)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    language = models.ForeignKey('localization.Language', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    ingredients = models.TextField(blank=True)

    class Meta:
        unique_together = ('food_item', 'language')
        verbose_name = _("Food Item Translation")
        verbose_name_plural = _("Food Item Translations")

    def __str__(self):
        return f"{self.food_item.name} - {self.language.code}"



class DietaryPreference(models.Model):
    """Stores dietary preferences."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = _("Dietary Preference")
        verbose_name_plural = _("Dietary Preferences")

    def __str__(self):
        return self.name

class DietaryPreferenceTranslation(models.Model):
    """Stores translations for dietary preferences."""
    id = models.AutoField(primary_key=True)
    language = models.ForeignKey('localization.Language', on_delete=models.CASCADE)
    dietary_preference = models.ForeignKey(DietaryPreference, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('language', 'dietary_preference')
        verbose_name = _("Dietary Preference Translation")
        verbose_name_plural = _("Dietary Preference Translations")

    def __str__(self):
        return f"{self.dietary_preference.name} - {self.language.code}"
    
class FoodItemDietaryInfo(models.Model):
    """Associates food items with dietary preferences."""
    id = models.AutoField(primary_key=True)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    dietary_info = models.ForeignKey(DietaryPreference, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('food_item', 'dietary_info')
        verbose_name = _("Food Item Dietary Info")
        verbose_name_plural = _("Food Item Dietary Info")

    def __str__(self):
        return f"{self.food_item.name} - {self.dietary_info.name}"
    
