from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
	modify_date = models.DateTimeField(null=True, blank=True)
	subject = models.CharField(max_length=200)
	content = models.TextField()
	create_date = models.DateTimeField()
	voter = models.ManyToManyField(User, related_name='voter_question')  # ��õ�� �߰�

	def __str__(self):
		return self.subject	

class Answer(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
	modify_date = models.DateTimeField(null=True, blank=True)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	content = models.TextField()
	create_date = models.DateTimeField()
	voter = models.ManyToManyField(User, related_name='voter_answer')  # ��õ�� �߰�
	


