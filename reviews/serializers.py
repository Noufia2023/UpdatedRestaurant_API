from rest_framework import serializers
from .models import Restaurant,Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields='__all__'
        


class RestaurantSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True) #List of reviews will be nested within the restaurant
    class Meta:
        model = Restaurant
        fields='__all__'
    