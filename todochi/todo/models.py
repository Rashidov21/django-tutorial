from django.db import models
from django_quill.fields import QuillField
# Create your models here.
STATUES = (
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
)


class Todo(models.Model):
    title = models.CharField(verbose_name="Todo", max_length=200)
    description = QuillField()
    created_at = models.DateTimeField(auto_now_add=True)
    doned_at = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=STATUES)
    
    class Meta:
        ordering = ["-id"]
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
        
    def __str__(self):
        return str(self.title)