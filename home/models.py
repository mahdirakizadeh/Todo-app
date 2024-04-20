from django.db import models


class Todo(models.Model):
    tittle = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField()

    def __str__(self):
        return f"{self.tittle} -- {self.created}"
