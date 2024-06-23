from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    """
    Модель курса обучения
    """
    course_name = models.CharField(max_length=100, verbose_name='название курса')
    image = models.ImageField(upload_to='curse', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='описание курса', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'курс обучения'
        verbose_name_plural = 'курсы обучения'


class Lesson(models.Model):
    """
    Модель урока связь с курсами через ForeignKey
    """
    lesson_name = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='lesson', verbose_name='Превью', **NULLABLE)
    url = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс обучения', related_name='lesson',
                               **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
