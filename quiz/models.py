from django.db import models

class Question(models.Model):
    content = models.TextField()
    answers = models.TextField()
    correct_answer = models.CharField(max_length = 1)

    def __str__(self):
        return str(self.id)
