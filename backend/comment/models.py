from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Tags"


class Comment(models.Model):
    text = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text}"

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = "Comments"
