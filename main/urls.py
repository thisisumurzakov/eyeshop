from django.urls import path
from .views import Picture_Upload

urlpatterns = [
    path('upload/', Picture_Upload.as_view()),
]
