from django.contrib import admin

from .models import Department, DepartmentPost
from .admin_forms import DepartmentAdminForm, DepartmentPostAdminForm


# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    form = DepartmentAdminForm

    list_display = ('name', 'is_main', 'status', 'created_time')

    fieldsets = (
        ('基本内容', {
            'description': '院系部门的基本内容',
            'fields': (
                'name',
                ('status', 'image'),
                'is_main',
                'created_time',
                'desc',
            ),
        }),
        ('额外内容', {
            'classes': ('collapse', ),
            'fields': (
                'number',
            )
        }),
    )


@admin.register(DepartmentPost)
class DepartmentPostAdmin(admin.ModelAdmin):
    form = DepartmentPostAdminForm

    list_display = ('name', 'department', 'status', 'created_time')
    list_display_links = []

    list_filter = ['department', ]
    search_fields = ['name', 'department__name']

    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True

    # 文章持有者自动生成
    exclude = ('owner', )

    fieldsets = (
        ('基本内容', {
            'description': '院系部门中文章的基本内容',
            'fields': (
                ('department', 'name'),
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
            'classes': ('collapse',),
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
        return super(DepartmentPostAdmin, self).save_model(request, obj, form, change)
