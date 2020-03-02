from django.db import models
from django.db.models import Q, F
from django.contrib.auth.models import User


# Create your models here.
class Department(models.Model):
    STATUS_NORMAL = 1
    STATUS_HIDDEN = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, "正常"),
        (STATUS_HIDDEN, "隐藏")
    )

    name = models.CharField(max_length=40, verbose_name="名称")
    desc = models.CharField(max_length=500, verbose_name="简介")
    image = models.ImageField(verbose_name="图片")
    is_main = models.BooleanField(default=False, verbose_name="是否为主要")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    created_time = models.DateTimeField(verbose_name="创建时间")
    number = models.PositiveIntegerField(default=0, verbose_name="人数")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "院系部门"
        ordering = ['-created_time']

    @classmethod
    def get_departments(cls):
        return cls.objects.filter(Q(status=cls.STATUS_NORMAL)&Q(is_main=True))

    @classmethod
    def get_communities(cls):
        return cls.objects.filter(Q(status=cls.STATUS_NORMAL)&Q(is_main=False))


class DepartmentPost(models.Model):
    """
    分类下所属的文章
    """
    STATUS_NORMAL = 1
    STATUS_HIDDEN = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, "正常"),
        (STATUS_HIDDEN, "隐藏")
    )

    plate_category = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="所属分类")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="持有者")
    name = models.CharField(max_length=40, verbose_name="名称")
    desc = models.CharField(max_length=200, verbose_name="文章摘要")
    content = models.TextField(verbose_name="文章内容")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    nov = models.PositiveIntegerField(default=0, verbose_name="访问人数")
    noc = models.PositiveIntegerField(default=0, verbose_name="评论人数")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "板块文章"
        ordering = ['-created_time']

    @classmethod
    def get_posts(cls):
        return cls.objects.filter(status=cls.STATUS_NORMAL).order_by('-nov')