from django.urls import path
from general import views

urlpatterns = [
    path('<int:zodiac>', views.zodiak_searcher),
    path('<str:zodiac>', views.zodiak_searcher),

]
