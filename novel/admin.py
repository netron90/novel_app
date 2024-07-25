from django.contrib import admin
from .models import User, Country, Category, Novel, Town
from django.utils import timezone
from django.db import models


# Register your models here.
# admin.site.register(User)
# admin.site.register(Country)
# admin.site.register(Category)
# admin.site.register(Town)

# class NovelAdmin(admin.ModelAdmin):
#     list_display = ('name', 'novel_number', 'date_start', 'category', 'country', 'town')
#     readonly_fields = ('novel_number', 'number')

#     def save_model(self, request, obj, form, change):
#         if not obj.novel_number:
#             today = timezone.now()
#             current_year_month = today.strftime('%Y%m')
#             max_number = Novel.objects.filter(
#                 date_start__year=today.year,
#                 date_start__month=today.month
#             ).aggregate(models.Max('number'))['number__max']
            
#             if max_number is not None:
#                 obj.number = max_number + 1
#             else:
#                 obj.number = 1

#             obj.novel_number = obj.generate_novel_number()
#         super().save_model(request, obj, form, change)

# admin.site.register(Novel, NovelAdmin)

from django.contrib import admin
from .models import User, Country, Category, Novel, Town, NovelImage
from django.utils import timezone

class NovelImageInline(admin.TabularInline):
    model = NovelImage
    extra = 1

class NovelAdmin(admin.ModelAdmin):
    list_display = ('name', 'novel_number', 'date_start', 'category', 'country', 'town')
    readonly_fields = ('novel_number', 'number')
    inlines = [NovelImageInline]

    def save_model(self, request, obj, form, change):
        if not obj.novel_number:
            today = timezone.now()
            current_year_month = today.strftime('%Y%m')
            max_number = Novel.objects.filter(
                date_start__year=today.year,
                date_start__month=today.month
            ).aggregate(models.Max('number'))['number__max']
            
            if max_number is not None:
                obj.number = max_number + 1
            else:
                obj.number = 1

            obj.novel_number = obj.generate_novel_number()
        super().save_model(request, obj, form, change)

admin.site.register(User)
admin.site.register(Country)
admin.site.register(Category)
admin.site.register(Novel, NovelAdmin)
admin.site.register(Town)

