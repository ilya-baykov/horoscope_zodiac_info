from django.urls import path
from general import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>', views.area_rectangle),
    path('square/<int:width>/', views.area_rectangle),
    path('circle/<int:radius>/', views.area_circle),

]
