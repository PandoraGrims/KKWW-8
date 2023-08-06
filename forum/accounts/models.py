# from django.db import models
#
# # Create your models here.
#
# from django.contrib.auth import get_user_model
#
#
# class User(models.Model):
#     name = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE,
#                                 verbose_name='Пользователь')
#     avatar = models.ImageField(null=True, blank=True, upload_to='avatars', verbose_name='Аватар')
#     password = models.CharField('Пароль', max_length=100)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = "profile"
#         verbose_name = 'Профиль'
#         verbose_name_plural = 'Профили'
