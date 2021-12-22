from django.db import models

# Create your models here.


class Page(models.Model):
    title = models.CharField(max_length=50, verbose_name="Titulo")
    content=models.TextField(verbose_name="contenido")
    slug= models.CharField(unique=True, max_length=150, verbose_name="URL")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")


    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"

    def __str__(self):
        return self.title