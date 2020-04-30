from django.urls import path,include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("events/<int:pk>/", views.EventDetailView.as_view(),name="event_detail"),
    path("events/new/", views.EventCreateView.as_view(),name="event_create"),
    path("events/<int:pk>/update/", views.EventUpdateView.as_view(),name="event_update"),
    path("events/<int:pk>/delete/", views.EventDeleteView.as_view(),name="event_delete"),
    path("events/<int:pk>/participate/", views.EventParticipateView.as_view(),name="event_participate"),
    path("sessions/<int:pk>/", views.SessionDetailView.as_view(),name="session_detail"),
    path("sessions/new/", views.SessionCreateView.as_view(),name="session_create"),
    path("sessions/<int:pk>/update/", views.SessionUpdateView.as_view(),name="session_update"),
    path("sessions/<int:pk>/delete/", views.SessionDeleteView.as_view(),name="session_delete"),
    path("spots/", views.SpotListView.as_view(),name="spot_list"),
    path("spots/<int:pk>/", views.SpotDetailView.as_view(),name="spot_detail"),
    path("spots/new/", views.SpotCreateView.as_view(),name="spot_create"),
    path("spots/<int:pk>/update/", views.SpotUpdateView.as_view(),name="spot_update"),
    path("spots/<int:pk>/delete/", views.SpotDeleteView.as_view(),name="spot_delete"),
]

