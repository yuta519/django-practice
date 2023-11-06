from django.urls import include, path
from rest_framework import routers

from snipets import views


router = routers.DefaultRouter()
router.register(r'snippets', views.SnippetList.as_view(), basename='snippet_list')
router.register(r'snippets/<int:pk>', views.SnippetDetail.as_view(), basename='snippet_detail')



urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view())
]
