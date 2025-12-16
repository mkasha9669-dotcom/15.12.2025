from django.db import models

# Create your models here

class Category (models.Model):
    name = models.CharField(max_length=225)
    is_active = models.BooleanField(default = True)
    parent_category = models.ForeignKey("self",on_delete=models.CASCADE, blank =True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        print("salom")
        super().save(*args, **kwargs)