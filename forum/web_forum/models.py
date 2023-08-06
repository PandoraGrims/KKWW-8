from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone


# class Project(models.Model):
#     name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Название')
#     description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
#     start_date = models.DateField(null=False, blank=False, verbose_name='Дата начала')
#     end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания')
#     user = models.ManyToManyField(User, related_name='projects', verbose_name='Юзер', blank=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = 'projects'
#         verbose_name = 'Проект'
#         verbose_name_plural = 'Проекты'


# class Type(models.Model):
#     type_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Тип')
#
#     def __str__(self):
#         return self.type_name
#
#     class Meta:
#         db_table = "types"
#         verbose_name = "Тип"
#         verbose_name_plural = "Типы"


# class Status(models.Model):
#     status_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Статус')
#
#     def __str__(self):
#         return self.status_name
#
#     class Meta:
#         db_table = "statuses"
#         verbose_name = "Статус"
#         verbose_name_plural = "Статусы"


class Answer(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Название")
    description = models.TextField(max_length=2000, verbose_name="Описание", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='answers', verbose_name='Проект')

    title = models.CharField(max_length=50, verbose_name="Название", unique=True, null=False, blank=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT,
                               default=1, related_name="discussions", verbose_name="Автор")





    def __str__(self):
        return f"{self.pk} {self.title}"

    class Meta:
        db_table = "answers"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


# class TaskType(models.Model):
#     task = models.ForeignKey('web_forum.Task', related_name='task_types', on_delete=models.CASCADE,
#                              verbose_name='Задача')
#     type = models.ForeignKey('web_forum.Type', related_name='type_tasks', on_delete=models.CASCADE, verbose_name='Тип')
#
#     def __str__(self):
#         return "{} | {}".format(self.task, self.type)


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
