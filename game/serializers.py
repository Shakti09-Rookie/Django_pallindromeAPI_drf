from rest_framework import serializers
from .models import Boards
from django.contrib.auth.models import User

class BoardSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    
    class Meta:
        model = Boards
        fields = (
            'id', 'user'
        )

    # def get_user(self, obj):
    #     print("hui", obj.user.id)
    #     return {
    #         'id':obj.user.id
    #     }

class getBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boards
        fields = (
            'id',
            'game_string',
        )

class updateBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boards
        fields = (
            'game_string',
        )

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boards
        fields = (
            'id',
        )