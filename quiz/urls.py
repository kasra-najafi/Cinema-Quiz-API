from quiz import views
from django.urls import path

urlpatterns = [
    path('quiz/', views.request_questions),
    path('answer/', views.result),
    
]