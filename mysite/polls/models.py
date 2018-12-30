from django.db import models

# Create your models here.

class Question(models.class (models.Model):
    question_text = models.models.CharField(max_length=200)
    pub_date = models.models.DateField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.models.IntegerField(default=0)