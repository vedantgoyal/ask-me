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

	question_body = models.CharField(max_length=255)
	source_id = models.CharField(max_length=20)
	source_link = models.CharField(max_length=255)
	source = models.CharField(max_length=20, choices=SOURCE_CHOICES)
	username = models.CharField(max_length=60)
	post_date = models.DateTimeField(default=timezone.now)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return f'{self.question_body}' 


class Answer(models.Model):

	question = models.ForeignKey('Question', on_delete=models.CASCADE)
	source_id = models.CharField(max_length=20)
	source_link = models.CharField(max_length=255)
	answer_body = models.CharField(max_length=255)
	is_best_answer = models.BooleanField()
	username = models.CharField(max_length=60)
	post_date = models.DateTimeField(default=timezone.now)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return f'{self.answer_body}' 