from django.urls import path
 
# importing views from views..py
from .views import create_view
 
urlpatterns = [
    path('', create_view),
]