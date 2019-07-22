from django.shortcuts import render

# Create your views here.
from .models import stock
from .serializers import stockserializer
from rest_framework import generics
from rest_framework.generics import ListAPIView,ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView,Request
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication,BasicAuthentication 
from rest_framework.permissions import IsAuthenticated
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
class stockList(generics.GenericAPIView,
                 mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.DestroyModelMixin):
    queryset = stock.objects.all()
    serializer_class = stockserializer
    lookup_field = 'id'
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,id=None):
        if id:
            return self.retrieve(Request)
        else:
            return self.list(request)
    def post(self, request):
        return self.create(request)
    def perform_create(self,serializer):
        serializer.save()
    def put(self, request ,id=None):
        return self.update(request,id)
    def perform_update(self,serializer):
        serializer.update(request,id)
    def delete(self , Request,id=None):
        return self.destroy(request)
    def perform_destroy(self,serializer):
        serializer.destroy(request)
class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
     


    
    
