from django.urls import path
from .views import *

urlpatterns = [
    path('', AcaraList.as_view()),
    path('detail/<str:id>/', AcaraDetail.as_view()),
    path('pembicara/', PembicaraList.as_view()),
    path('pembicara/<str:id>/', PembicaraDetail.as_view()),
]
