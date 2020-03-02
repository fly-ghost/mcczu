from django.contrib import admin

from .models import Plate, PlateCategory, PlatePost
from .admin_forms import PlateAdminForm, PlatePostAdminForm


# Register your models here.
@admin.register(Plate)
class PlateAdmin(admin.ModelAdmin):
    form = PlateAdminForm

    list_display = ('name', 'status', 'weight', 'created_time')

    fieldsets = (
        ('基本内容', {
            'description': '板块基本内容',
            'fields': (
                'name',
                ('status', 'image'),
            ),
        }),
        ('可选内容', {
            'fields': (
                'desc',
            ),
        }),
        ('额外内容', {
            'classes': ('collapse', ),
            'fields': (
                ('nop', 'noc'),
                'weight',
            ),
        })
    )


@admin.register(PlateCategory)
class PlateCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'plate', 'status', 'created_time')

    fieldsets = (
        ('基本内容', {
            'description': '板块中分类的基本内容',
            'fields': (
                ('plate', 'name'),
                ('status', 'image'),
            ),
        }),
        ('额外信息', {
            'classes': ('collapse', ),
            'fields': (

            ),
        })
    )


@admin.register(PlatePost)
class PlatePostAdmin(admin.ModelAdmin):
    form = PlatePostAdminForm

    list_display = ('name', 'category', 'status', 'created_time')

    list_filter = ['category', ]
    search_fields = ['name', 'category__name']

    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True

    # 文章作者会自动绑定
    exclude = ('owner', )

    fieldsets = (
        ('基本内容', {
            'description': '板块中文章的基本内容',
            'fields': (
                ('category', 'name'),
                'status',
            ),
        }),
        ('可选内容', {
            'fields': (
                'desc',
            ),
        }),
        ('主体内容', {
            'fields': (
                'content',
            ),
        }),
        ('额外内容', {
            'classes': ('collapse', ),
            'fields': (
                ('nov', 'noc'),
            ),
        })
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
        return super(PlatePostAdmin, self).save_model(request, obj, form, change)
