from rest_framework import serializers
from todo.models import Todo


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todo
        fields = ('title','description','created_at','doned_at','done','status')