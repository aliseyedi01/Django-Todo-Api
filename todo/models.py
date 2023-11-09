from django.db import models
from django.contrib.auth.models import User
import uuid


class Category(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True)
    count = models.IntegerField(default=0, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.count = Task.objects.filter(category=self).count()
        super().save(*args, **kwargs)




class Task(models.Model):
    uuid = models.UUIDField(editable = False, primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title




