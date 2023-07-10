from django.urls import path, include
from .views import *

app_name = 'pets'
urlpatterns = [
    path('pets', PetCreateView.as_view()),
    path('all/', PetListView.as_view()),
    path('details/<int:pk>', PetDetailViews.as_view()),
]
