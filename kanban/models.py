from django.db import models

# Create your models here.


class Board(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)


class Category(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)


class Card(models.Model):
    title = models.TextField(max_length=50)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="cards")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="category",
        null=True,
        default=None,
    )
