from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
     path(
         r'events/', views.events_list.as_view(), name='events_list'),
     path(
         r'events/<uuid:pk>/', views.event_detail.as_view(),
         name='event_detail'),
     path(
         r'reporters/', views.reporters_list.as_view(),
         name='reporter_list'),
     path(
         r'reporters/events/<int:reporter_id>/', views.reporter_events.as_view(),
         name='reporter_events'),
     path(
        r'types/', views.types_list.as_view() ,
        name='types_list'),
     path(
         r'types/<int:type_id>/', views.events_per_type.as_view(),
         name='events_per_type'),
]
