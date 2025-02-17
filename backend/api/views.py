# from rest_framework.decorators import APIView
# from rest_framework import generics
# from rest_framework import mixins
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from .serializers import ArticleSerializer, CategorySerializer
from .models import Article, Categories
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

# Create your views here.


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [FormParser, MultiPartParser, JSONParser]
    
    def get_user(self):
        user = self.request.user
        return user
    
    def perform_create(self, serializer):
        user = self.get_user()
        print(user)
        serializer.save(author=user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
        



# class ArticleViewSet(viewsets.ViewSet):
    
#     def list(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def retrieve(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset,pk=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
    
#     def update(self, request, pk=None):
#         article = Article.objects.get(pk=pk)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def destroy(self, request, pk=None):
#         article = Article.objects.get(pk=pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

    
#     def partial_update(self, request, pk=None):
#         pass

# class ArticleList(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ArticleDetail(APIView):
#     def get_object(self, id):
#         try:
#             article = Article.objects.get(id=id)
#             return article
#         except Article.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
    
#     def get(self, request, id):
#         article = self.get_object(id=id)
#         serialiser = ArticleSerializer(article)
#         return Response(serialiser.data)
    
#     def put(self, request, id):
#         article = self.get_object(id=id)
#         serialiser = ArticleSerializer(article, data=request.data)
#         if serialiser.is_valid():
#             serialiser.save()
#             return Response(serialiser.data)
#         return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request, id):
#         article = self.get_object(id=id)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)