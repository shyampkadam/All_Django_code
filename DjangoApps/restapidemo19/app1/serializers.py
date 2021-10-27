from rest_framework import serializers

from app1.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'pub_date', 'author','isbn','storename']