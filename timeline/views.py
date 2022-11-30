from timeline.serializers import EventSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Event

# Create your views here.
#localhost:8000/events/ get post
#localhost:8000/events/:id get delete update
class EventsView(APIView):
    """View class for events/ for viewing all and creating"""
    #index class based view
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response({'events': serializer.data})

class EventsDetailView(APIView):
    """View class for events/:pk for viewing a single event, updating a single event, or removing a single event"""
