from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return f"{self.author} added {self.title} on {self.created_at}"

class Comment(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return f"{self.author} added {self.title} on {self.created_at}"

class Plan(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return f"{self.author} added {self.title} on {self.created_at}"