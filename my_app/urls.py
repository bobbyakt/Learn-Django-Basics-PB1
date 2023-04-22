from django.urls import path
from my_app.views import hello_world,hello_temp

urlpatterns = [
    path('hello', hello_world),
    path('hello_temp', hello_temp)
]
