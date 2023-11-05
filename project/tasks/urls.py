from django.urls import path

from tasks import views


app_name = "tasks"

urlpatterns = [
    path("users/", views.UserIndexView.as_view(), name="users"),
    path("users/<int:pk>", views.UserDetailView.as_view(), name="user_detail"),
    path("tickets/", views.TicketIndexView.as_view(), name="tickets"),
    path("tickets/<int:pk>", views.TicketDetailView.as_view(), name="ticket_detail"),
]
