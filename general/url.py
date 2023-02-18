from django.urls import path
from general import views

urlpatterns = [
    path('<zodiac>', views.zodiak_searcher),

]
