from django.urls import path
from .views import PostsListView, PostDetailView


urlpatterns = [
    path('', PostsListView.as_view()),
    path('<int:pk>', PostDetailView.as_view()),
]


