from rest_framework import generics
from todo.models import Todo
from .serializers import BookSerializer



class BookAPIView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = BookSerializer