from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=250, verbose_name='주제 이름')

    def __str__(self):
        return self.categoryName

    class Meta:
        db_table = '카테고리'
        verbose_name = '카테고리'

class Board(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, verbose_name='작성자')
    title = models.CharField(max_length=128, verbose_name='제목')
    descriptions = models.TextField(verbose_name='내용')
    hits = models.PositiveIntegerField(verbose_name='조회수', default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="최종수정일")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="카테고리 이름")

    def __str__(self):
        return self.title

    class Meta:
        db_table = '게시판'
        verbose_name = '게시판'

