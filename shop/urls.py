from django.urls import path
from .views import CategoryListView, ProductListView, ProductListAllView

urlpatterns = [
    path('category/<int:pk>/', ProductListView.as_view()),
    path('all/', ProductListAllView.as_view()),
    path('category/<slug:gender>/', CategoryListView.as_view()),
]
