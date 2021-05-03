from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):

	# Source Enum values
	SOURCE_GUS = 'Gus'
	SOURCE_SLACK = 'Slack'

	# Enum for Source
	SOURCE_CHOICES = (
		(SOURCE_GUS, 'GUS'),
		(SOURCE_SLACK, 'Slack'),
		)

	question_content = models.CharField(max_length=255)
	source_id = models.CharField(max_length=20)
	source_link = models.CharField(blank=True, null=True, max_length=255)
	source = models.CharField(blank=True, null=True, max_length=20, choices=SOURCE_CHOICES)
	best_answer = models.CharField(blank=True, null=True, max_length=255)
	best_answer_url = models.CharField(blank=True, null=True, max_length=255)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return f'{self.question_content}' 


class Answer(models.Model):

	question = models.ForeignKey('Question', on_delete=models.CASCADE)
	reply_id = models.CharField(max_length=20)
	source_id = models.CharField(max_length=20)
	answer_body = models.CharField(blank=True, null=True, max_length=255)
	is_best_answer = models.BooleanField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return f'{self.answer_body}' 
