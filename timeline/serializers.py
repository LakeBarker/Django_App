from rest_framework import serializers

from .models import Event, Comment, Plan

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Event

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Comment

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Plan