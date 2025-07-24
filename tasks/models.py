from django.db import models
from django.utils import timezone
from datetime import timedelta

class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
        (4, 'Critical'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    deadline_days = models.IntegerField(help_text="Number of days until deadline")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['deadline_days', '-priority', 'created_at']
    
    def __str__(self):
        return self.title
    
    @property
    def get_priority_display_color(self):
        colors = {
            1: 'success',  # Green for Low
            2: 'info',     # Blue for Medium
            3: 'warning',  # Orange for High
            4: 'danger',   # Red for Critical
        }
        return colors.get(self.priority, 'secondary')
    
    @property
    def is_urgent(self):
        return self.deadline_days <= 3 and self.priority >= 3
