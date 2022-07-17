from django.contrib import admin
from .models import Image
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class ImageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'ImgName', 'image', 'short_description')
    search_fields =['ImgName']
    ordering = ['id']
    readonly_fields = ['image', 'short_description']
    save_as = True
    save_on_top = True

    def image(self, obj):
        return mark_safe('<img src="{url}" width="150" height="150"/>'.format(
            url = obj.ImgURL,
        )
    )

admin.site.register(Image, ImageAdmin)

# admin.site.register(Image)
