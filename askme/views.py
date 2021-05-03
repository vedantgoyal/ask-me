from django.shortcuts import render
from django.apps import apps

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import QuestionSerializer
from .models import Question


class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class MyOwnView(APIView):
    def get(self, request):
        return Response({'some': 'data'})
