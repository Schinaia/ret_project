from django.db import models

from django.db import models
from django.urls import reverse
from datetime import datetime

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        
        return f'<a href="{url}"> {self.title} </a>'
