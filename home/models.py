from django.db import models

class Link(models.Model):
  url = models.URLField()
  title = models.CharField(max_length=200)
  description = models.TextField(blank=True, default='')

  def __str__(self):
      return self.title
