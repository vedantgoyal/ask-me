from rest_framework import serializers

from .models import Question
from .models import Answer

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = (
            "id",
            "question_content",
            "source_id",
            "source",
            "source_link",
            "best_answer",
            "best_answer_url",
        )

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = (
            "id",
            "question",
            "reply_id",
            "source_id",
            "answer_body",
            "is_best_answer",
        )