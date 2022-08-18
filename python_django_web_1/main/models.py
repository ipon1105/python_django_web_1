from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title + "|" + self.task
        pass

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        pass

    pass


class User(models.Model):
    username = models.CharField('ИмяПользователя', max_length=50)
    password = models.CharField('Пароль', max_length=50)

    def __str__(self):
        return self.username + "|" + self.password
        pass

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        pass

    pass
