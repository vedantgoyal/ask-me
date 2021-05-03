from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import QuestionSerializer
from .models import Question
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector


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