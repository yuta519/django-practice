from django.urls import path

from tasks import views


app_name = "tasks"

urlpatterns = [
    path("users/", views.UserIndexView.as_view(), name="users")
]
