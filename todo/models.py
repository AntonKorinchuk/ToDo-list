from django.db import models


class Task(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    marker = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks")

    class Meta:
        ordering = ("marker", "-created")

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
