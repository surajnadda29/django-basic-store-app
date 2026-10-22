from django.urls import path
from .views import myfunc
urlpatterns = [
    path('',myfunc)
]
