from __future__ import unicode_literals

from djongo import models


class Photo(models.Model):
    # Auto updated when data is inserted
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    # Auto updated when data is altered
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    # Documents
    title = models.CharField(max_length=100)
    jpg = models.ImageField(upload_to='gallery/photos/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.jpg.delete()
        super().delete(*args, **kwargs)
