from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
      path('new', views.add_note, name='add_note'),\
      path('edit/<int:pk>/', views.edit_note, name='edit'),
      path('delete/<int:pk>/', views.delete_note, name='delete'),
      path('search/', views.search_view, name='search'),
]