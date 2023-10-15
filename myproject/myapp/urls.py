from django.urls import path
from . import views

urlpatterns = [
    path('generate_data/', views.generate_data, name='generate_data'),
]
