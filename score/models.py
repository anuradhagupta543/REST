from django.db import models


class HighScore(models.Model):
    name = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return self.name
