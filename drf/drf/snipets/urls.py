from django.urls import include, path
from rest_framework import routers

from snipets import views


router = routers.DefaultRouter()
# router.register(r'snippets', views.SnippetList.as_view(), basename='snippet_list')
# router.register(r'snippets/<int:pk>', views.SnippetDetail.as_view(), basename='snippet_detail')
router.register(r'users', views.UserViewSet)



urlpatterns = router.urls + [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]
