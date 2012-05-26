from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=1000)
    ask_date = models.DateTimeField('date asked')

class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer = models.CharField(max_length=2000)
    answer_date = models.DateTimeField('date answered')
