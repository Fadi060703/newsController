from django.shortcuts import get_object_or_404
from rest_framework import status 
from rest_framework.response import Response 
from rest_framework.request import Request 
from rest_framework.views import APIView 
from .models import * 
from .serializers import *
# Create your views here.

class ListCreateArticleView( APIView ) :
    serializer_class = ArticleSerializer 
    
    def get( self , req : Request ) :
        articles = Article.objects.all() 
        serializer = self.serializer_class( articles , many = True ) 
        return Response( data = serializer.data , status = status.HTTP_200_OK ) 
    
    def post( self , req : Request ) :
        data = req.data 
        serializer = self.serializer_class( data = data ) 
        if serializer.is_valid():
            serializer.save() 
            return Response( status = status.HTTP_201_CREATED ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST ) 
    
class ArticleDetailView( APIView ) :
    serializer_class = ArticleSerializer 
    
    def get( self , req : Request , pk : int ) :
        article = get_object_or_404( Article , pk = pk ) 
        serializer = self.serializer_class( article ) 
        return Response( data = serializer.data , satus = status.HTTP_200_OK ) 
    
    def delete( self , req : Request , pk : int ) :
        article = get_object_or_404( Article , pk = pk ) 
        article.delete() 
        return Response( status = status.HTTP_200_OK ) 
    

 
