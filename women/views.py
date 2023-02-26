from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Women, Category
from .serializers import Womenserializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework.decorators import action

from rest_framework.permissions import IsAuthenticatedOrReadOnly

class WomenViewSet(viewsets.ModelViewSet):
    # queryset = Women.objects.all()

    serializer_class = Womenserializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Women.objects.all()[:3]

        return Women.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)

        return Response({'cats': cats.name})



#
# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#
#     serializer_class = Womenserializer
#
#
# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#
#     serializer_class = Womenserializer
#
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#
#     serializer_class = Womenserializer



