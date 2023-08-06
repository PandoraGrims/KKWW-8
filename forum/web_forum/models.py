from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone


class Discussion(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название", unique=True, null=False, blank=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT,
                               default=1, related_name="discussions", verbose_name="Автор")
    description = models.TextField(max_length=2000, verbose_name="Описание", null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")

    def str(self):
        return f"{self.id} {self.title}"

    class Meta:
        db_table = "discussions"
        verbose_name = "Дискуссия"
        verbose_name_plural = "Дискуссии"


class Answer(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Имя комментатора')
    description = models.TextField(max_length=2000, verbose_name="Описание", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='answers',
                                   verbose_name='Дискуссия')

    def __str__(self):
        return f"{self.pk} {self.name}"

    class Meta:
        db_table = "answers"
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
