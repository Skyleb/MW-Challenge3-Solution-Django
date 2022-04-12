# models.py
from django.db import models

class ContainerContent(models.Model):
  iconPath = models.CharField(max_length=60)
  title = models.CharField(max_length=60)
  content = models.CharField(max_length=500)

  def __str__(self):
    return str(self.id)


class ContactContainerContent(models.Model):
  title = models.CharField(max_length=60)
  content = models.CharField(max_length=500)

  def __str__(self):
    return str(self.id)


class ContactInfo(models.Model):
  first_name = models.CharField(max_length=60)
  last_name = models.CharField(max_length=60)
  title = models.CharField(max_length=60)
  email = models.CharField(max_length=60)
  message = models.CharField(max_length=500)

  def __str__(self):
    return str(self.id)