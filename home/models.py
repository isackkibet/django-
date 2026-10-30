from django.db import models
from django.urls import reverse


class Challenge(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    flag = models.CharField(max_length=120, help_text='The answer players must submit.')
    points = models.PositiveIntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home:challenge_detail', args=[self.pk])

    def check_flag(self, submitted):
        return submitted.strip().lower() == self.flag.strip().lower()
