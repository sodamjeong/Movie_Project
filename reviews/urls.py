from django.urls import path
from . import views

app_name = "reviews"
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('delete/<int:review_pk>/', views.delete, name='delete'),
    path('<int:review_pk>/', views.detail, name='detail'),
    path('update/<int:review_pk>/', views.update, name='update'),
    path('comment/<int:review_pk>/', views.comment_create, name='comment_create'),
    path('comment/<int:review_pk>/delete/<int:comment_pk>/', views.comment_delete, name='comment_delete'),
    path('likes/<int:review_pk>/', views.likes, name='likes'),
]
