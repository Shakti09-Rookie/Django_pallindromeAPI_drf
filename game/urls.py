from django.urls import path
from .views import create, getBoard, updateBoard, updateBoarda, listview

urlpatterns = [
    path('', create, name='create-game'),
    path('all/', listview, name='list-game'),
    path('<int:id>/', getBoard, name='get-game-id'),
    path('<int:id>/update/', updateBoard, name='update-game'),
    path('<int:id>/updatee/', updateBoarda, name='update-game'),
]
