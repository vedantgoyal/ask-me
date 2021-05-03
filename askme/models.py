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

	question_content = models.CharField(max_length=60)
	source_id = models.CharField(max_length=20)
	source_link = models.CharField(blank=True, null=True, max_length=20)
	source = models.CharField(blank=True, null=True, max_length=20, choices=SOURCE_CHOICES)
	best_answer = models.CharField(blank=True, null=True, max_length=60)
	best_answer_url = models.CharField(blank=True, null=True, max_length=255)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	#address = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return f'{self.question_content}' 
