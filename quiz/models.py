from django.db import models
from log.models import Program

class Quiz(models.Model):
    """creating quiz models"""
    title = models.CharField(max_length=255)
    program= models.ForeignKey(Program, on_delete=models.CASCADE)
    duration = models.IntegerField
    question_set = models.JSONField(default=list, blank=True)
    class Meta:
        verbose_name_plural = 'Quizes'

    def __str__(self) :
        return self.title
