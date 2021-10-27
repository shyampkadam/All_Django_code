from django.shortcuts import render

# Create your views here.
from rest_framework import generics, filters
from rest_framework.filters import OrderingFilter

from app1.models import Book
from app1.serializers import BookSerializer


class BookAPIView(generics.ListCreateAPIView):
    #search_fields = ['author','isbn']
    filter_backends = (filters.SearchFilter,filters.OrderingFilter)
    search_fields = ('author',)
    ordering_fields = ('pub_date',)
    queryset = Book.objects.all()
    serializer_class = BookSerializer