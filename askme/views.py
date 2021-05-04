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
        query = SearchQuery(self.request.query_params.get('query'), search_type='phrase')
        limit = self.request.query_params.get('limit') or 100
        offset = self.request.query_params.get('offset') or 0
        vector = SearchVector('question_body')
        if query:
            queryset = queryset.annotate(rank=SearchRank(vector, query)).order_by('-rank')[int(offset):int(offset)+int(limit)]
        return queryset

class AnswerView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer