from rest_framework import serializers
from .serializers import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title','category','description','image']