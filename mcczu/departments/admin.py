from django.contrib import admin

from .models import Department, DepartmentPost


# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_main', 'status', 'created_time')

    fields = (
        'name',
        'desc',
        'image',
        'is_main',
        'status',
        'number',
    )


@admin.register(DepartmentPost)
class DepartmentPostAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'status', 'created_time')
    list_display_links = []

    list_filter = ['department']
    search_fields = ['name', 'department__name']

    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True

    fields = (
        ('department', 'name'),
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
        return super(DepartmentPostAdmin, self).save_model(request, obj, form, change)