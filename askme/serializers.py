from rest_framework import serializers

from .models import Question
from .models import Answer

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = (
            "id",
            "question_body",
            "source_id",
            "source_link",
            "source",
            "username",
            "post_date",
        )

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = (
            "id",
            "question_id",
            "source_id",
            "source_link",
            "answer_body",
            "is_best_answer",
            "username",
            "post_date",
        )