from django.urls import path
from general import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>', views.area_rectangle),


]
