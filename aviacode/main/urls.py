from django.urls import path, include
from .views import *
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('task_template/<int:pk>/', TaskDetailView.as_view(), name='task_template'),
    
]