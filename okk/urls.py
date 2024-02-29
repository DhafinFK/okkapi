from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('init-fakul/', create_initial_fakultas, name='create-fakul'), 
    path('init-bidang/', create_bidang_kepanitiaan, name='create-kepaniataan'),
    path('fakultas/', FakultasList.as_view()),
    path('fakultas/<str:name>/', FakultasDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)