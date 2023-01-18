from django.urls import path
from .views import *

urlpatterns = [
    path('list', ListUser.as_view()),
    path('create/', CreateUser.as_view()),
    path('update/id/<int:pk>/', UpdateUser.as_view()),
    path('delete/id/<int:pk>/', DeleteUser.as_view()),
]
