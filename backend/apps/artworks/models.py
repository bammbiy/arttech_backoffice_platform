from django.db import models


class Artwork(models.Model):
    title = models.CharField("작품명", max_length=200)
    artist = models.CharField("작가명", max_length=100)
    price = models.PositiveIntegerField("가격")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} - {self.artist}"
