from django.db import models

class Flashcard(models.Model):
    CATEGORY_CHOICES = [
        ('investing', 'Investing'),
        ('trading', 'Trading'),
    ]

    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='investing')

    def __str__(self):
        return self.question
