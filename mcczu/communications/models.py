from django.db import models
from django.db.models import Q, F
from django.contrib.auth.models import User


# Create your models here.
class Plate(models.Model):
    """
    板块主体
    """
    STATUS_NORMAL = 1
    STATUS_HIDDEN = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, "正常"),
        (STATUS_HIDDEN, "隐藏")
    )

    name = models.CharField(max_length=40, unique=True, verbose_name="名称")
    desc = models.CharField(max_length=200, blank=True, null=True, verbose_name="简介")
    image = models.ImageField(verbose_name="图片")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    nop = models.PositiveIntegerField(default=0, verbose_name="板块人数")
    noc = models.PositiveIntegerField(default=0, verbose_name="评论人数")
    weight = models.PositiveIntegerField(default=1, choices=zip(range(1, 8), range(1, 8)),
                                         help_text="权重高者在前", verbose_name="权重")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "板块"
        ordering = ['-created_time']

    @classmethod
    def get_plates(cls):
        """
        返回各个板块
        :return:
        """
        return cls.objects.filter(status=cls.STATUS_NORMAL).order_by('-weight')


class PlateCategory(models.Model):
    """
    板块中的一些分类
    """
    STATUS_NORMAL = 1
    STATUS_HIDDEN = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, "正常"),
        (STATUS_HIDDEN, "隐藏")
    )

    plate = models.ForeignKey(Plate, on_delete=models.CASCADE, verbose_name="所属板块")
    name = models.CharField(max_length=40, verbose_name="名称")
    image = models.ImageField(verbose_name="图片")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "板块中的分类"
        ordering = ['-created_time']

    @classmethod
    def get_categories(cls):
        return cls.objects.filter(status=cls.STATUS_NORMAL).order_by('-created_time')


class PlatePost(models.Model):
    """
    分类下所属的文章
    """
    STATUS_NORMAL = 1
    STATUS_HIDDEN = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, "正常"),
        (STATUS_HIDDEN, "隐藏")
    )

    plate_category = models.ForeignKey(PlateCategory, on_delete=models.CASCADE, verbose_name="所属分类")
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
