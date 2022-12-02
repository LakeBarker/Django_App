from timeline.serializers import EventSerializer, CommentSerializer, PlanSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Event, Comment, Plan

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
    
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTML_400_BAD_REQUEST)

class EventDetailView(APIView):
    """View class for events/:pk for viewing a single event, updating a single event, or removing a single event"""
    def get(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        serializer = EventSerializer(event)
        return Response({'event': serializer.data})

    def patch(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTML_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        event.delete()
        return Response(status=status.HHTP_204_NO_CONTENT)

class CommentsView(APIView):
    """View class for events/ for viewing all and creating"""
    #index class based view
    def get(self, request):
        comments = Comment.objects.all()
        serializer = EventSerializer(comments, many=True)
        return Response({'comments': serializer.data})
    
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTML_400_BAD_REQUEST)

class CommentDetailView(APIView):
    """View class for events/:pk for viewing a single comment, updating a single event, or removing a single event"""
    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(comment)
        return Response({'comment': serializer.data})

    def patch(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = EventSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTML_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return Response(status=status.HHTP_204_NO_CONTENT)

class PlansView(APIView):
    """View class for events/ for viewing all and creating"""
    #index class based view
    def get(self, request):
        plans = Plan.objects.all()
        serializer = PlanSerializer(plans, many=True)
        return Response({'plans': serializer.data})
    
    def post(self, request):
        serializer = PlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTML_400_BAD_REQUEST)

class PlanDetailView(APIView):
    """View class for plans/:pk for viewing a single plan, updating a single plan, or removing a single plan"""
    def get(self, request, pk):
        plan = get_object_or_404(Plan, pk=pk)
        serializer = PlanSerializer(plan)
        return Response({'plan': serializer.data})

    def patch(self, request, pk):
        plan = get_object_or_404(Plan, pk=pk)
        serializer = PlanSerializer(plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTML_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        plan = get_object_or_404(Plan, pk=pk)
        plan.delete()
        return Response(status=status.HHTP_204_NO_CONTENT)
