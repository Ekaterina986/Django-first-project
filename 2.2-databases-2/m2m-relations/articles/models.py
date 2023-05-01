from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Relationship(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='articles')
    teg = models.ForeignKey('Teg', on_delete=models.CASCADE, related_name='tegs')
    object =models.ForeignKey('Object', on_delete=models.CASCADE, related_name='objects')
    scope = models.ForeignKey('Scope', on_delete=models.CASCADE, related_name='scope')


class Teg(models.Model):
    name = models.CharField(max_length=20)
    Relationship = models.ManyToManyField(
        Article,
        through='Relationship',
        through_fields=('teg', 'article'),
        related_name='tegs',
    )


class Object(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='articles')
    teg = models.ForeignKey(Teg, on_delete=models.CASCADE, related_name='tegs')


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name = 'articles')
    teg = models.ForeignKey(Teg, on_delete=models.CASCADE, related_name = 'tegs')
    _is_main = models.ExclusiveBooleanField(default=False, on=('teg',))
    