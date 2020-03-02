from django.contrib import admin

from .models import Plate, PlateCategory, PlatePost


# Register your models here.
@admin.register(Plate)
class PlateAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'weight', 'created_time')

    fields = (
        'name',
        'desc',
        'image',
        'status',
        ('nop', 'noc'),
        'weight',
    )


@admin.register(PlateCategory)
class PlateCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'plate', 'status', 'created_time')

    fields = (
        ('plate', 'name'),
        'image',
        'status',
    )


@admin.register(PlatePost)
class PlatePostAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'status', 'created_time')
    list_display_links = []

    list_filter = ['category', ]
    search_fields = ['name', 'category__name']

    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True

    fields = (
        ('category', 'name'),
        'desc',
        'content',
        'status',
        'owner',
        ('nov', 'noc'),
    )

    def save_model(self, request, obj, form, change):
        """
        自动保存对应作者
        :param request:
        :param obj:
        :param form:
        :param change:
        :return:
        """
        obj.owner = request.user
        return super(PlateAdmin, self).save_model(request, obj, form, change)
