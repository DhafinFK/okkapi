from django.urls import path
from .views import *

urlpatterns = [
    path('', AcaraList.as_view()),
    path('<str:id>/', AcaraDetail.as_view()),
]
