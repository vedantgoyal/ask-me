from django.apps import apps
from django.http import JsonResponse
from django.shortcuts import render

from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import QuestionSerializer, AnswerSerializer
from .models import Question, Answer


class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class MyOwnView(APIView):
    def get(self, request):
        return Response({'some': 'data'})