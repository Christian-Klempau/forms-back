from rest_framework import serializers
from .models import Board, Card, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"


class CardDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Card
        fields = "__all__"


class BoardSerializer(serializers.ModelSerializer):
    cards = CardDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = "__all__"
