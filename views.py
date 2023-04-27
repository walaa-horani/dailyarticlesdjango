from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
# Create your views here.
from rest_framework import viewsets

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

