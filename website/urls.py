from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
     path(
         'events/', views.events_list.as_view(), name='events_list'),
     path(
         'events/<uuid:pk>/', views.event_detail.as_view(),
         name='event_detail'),
     path(
         'reporters/', views.reporters_list.as_view(),
         name='reporter_list'),
     path('reporters/events/<int:pk>/', views.reporter_events.as_view(),
          name='reporter_events')
]
