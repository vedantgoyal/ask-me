from rest_framework import serializers

from .models import Question

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('question_content', 'source_id', 'source_link', 'source', 'best_answer', 'best_answer_url')