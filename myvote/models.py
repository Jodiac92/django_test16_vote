from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 100)
    pub_date = models.DateTimeField()
    
    def __str__(self):
        return self.question_text #1,2로 안나오고 좋아하는 운동,친구 등 으로 나옴
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 20)
    votes = models.IntegerField(default = 0)
    
