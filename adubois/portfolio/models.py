from django.db import models


class MyWorks(models.Model):
    title = models.CharField('Название', max_length=30)
    descriptions = models.TextField('Описание', max_length=30)
    image = models.ImageField(upload_to='portfolio/', blank=True, null=True,
                              verbose_name='Картина')
    date = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Моя работа'
        verbose_name_plural = 'Мои работы'
