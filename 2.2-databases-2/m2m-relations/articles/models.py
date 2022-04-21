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


class Scope(models.Model):
    name = models.CharField(
        max_length=30, verbose_name='Название раздела'
    )
    articles = models.ManyToManyField(
        Article, related_name='tags', through="ArticleScope"
    )

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['name']

    def __str__(self):
        return self.name


class ArticleScope(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.PROTECT,
        related_name='scopes',
        verbose_name='Статья'
    )
    tag = models.ForeignKey(
        Scope,
        on_delete=models.PROTECT,
        related_name='scopes',
        verbose_name='Раздел'
    )
    is_main = models.BooleanField(verbose_name='Основной раздел', default=False)

    class Meta:
        verbose_name = 'Раздел статьи'
        verbose_name_plural = 'Разделы статьи'
        unique_together = ('article', 'tag')
        ordering = ['-is_main', 'tag']
        constraints = (
            models.UniqueConstraint(
                fields=('article', 'is_main'),
                name='one_main_constraint',
                condition=models.Q(is_main=True)
            ),
        )
