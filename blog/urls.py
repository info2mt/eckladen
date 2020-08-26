from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('<category_name>/', views.blog_category, name='blog_category'),
    path("create/post/", views.PostCreate.as_view(), name="post_create"),
]