from django.urls import path
from .views import *

urlpatterns = [
    path('', MahasiswaList.as_view()),
    path('mentor/', MentorList.as_view()),
    path('mentor/<str:id>/', MentorDetail.as_view()),
    path('mentee/', MenteeList.as_view()),
    path('mentee/<str:id>/', MenteeDetail.as_view()),
    path('panitia/', PanitiaList.as_view()),
    path('panitia/<str:id>/', PanitiaDetail.as_view()),
    path('detail/<str:id>/', MahasiswaDetail.as_view()),
]