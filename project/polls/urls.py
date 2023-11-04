from django.urls import path

from polls import views

urlpatterns = [
    path("", views.index, name="polls index"),
    path("<int:question_id>/", views.detail, name="polls detail"),
    path("<int:question_id>/results/", views.results, name="polls results"),
    path("<int:question_id>/vote/", views.vote, name="polls vote"),
]
