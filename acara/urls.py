from django.urls import path
from .views import *

urlpatterns = [
    path('', AcaraList.as_view()),
    path('detail/<str:id>/', AcaraDetail.as_view()),
    path('pembicara/', PembicaraList.as_view()),
    path('pembicara/<str:id>/', PembicaraDetail.as_view()),
    path('sponsor/', SponsorList.as_view()),
    path('sponsor/<str:id>/', SponsorDetail.as_view()),
    path('sponsor-acara/', SponsorAcaraList.as_view()),
    path('sponsor-acara/<str:id>/', SponsorAcaraDetail.as_view()),
]
