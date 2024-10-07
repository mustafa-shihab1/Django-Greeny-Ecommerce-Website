from django.urls import path, include
from rest_framework import routers
from .api import ToDoAPIViewSet


router = routers.DefaultRouter()
router.register('todo', ToDoAPIViewSet)

app_name = 'todo'

urlpatterns = [
    path('', include(router.urls))
]

