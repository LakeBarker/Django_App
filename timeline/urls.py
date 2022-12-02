from django.conf.urls import include
from django.urls import path
from .views import EventsView, EventDetailView, CommentsView, CommentDetailView, PlansView, PlanDetailView

urlpatterns = [
    path('', EventsView.as_view(), name='events'),
    path('<int:pk>/', EventDetailView.as_view(), name='event'),
    path('', CommentsView.as_view(), name='comments'),
    path('<int:pk>/', CommentDetailView.as_view(), name='comment'),
    path('', PlansView.as_view(), name='plans'),
    path('<int:pk>/', PlanDetailView.as_view(), name='plan'),
]