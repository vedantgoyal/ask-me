from django.apps import apps
from django.http import JsonResponse
from django.shortcuts import render

from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from .serializers import QuestionSerializer, AnswerSerializer
from .models import Question, Answer


class QuestionView(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer    

    def get_queryset(self):
        queryset = Question.objects.all()
        query = self.request.query_params.get('query')
        limit = self.request.query_params.get('limit')
        vector = SearchVector('question_content')
        if not limit:
            limit = 5
        if query:
            queryset = queryset.annotate(rank=SearchRank(vector, query)).order_by('-rank')[:int(limit)]
        return queryset

class AnswerView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer