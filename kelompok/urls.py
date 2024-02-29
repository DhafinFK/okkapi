from django.urls import path
from .views import *

urlpatterns = [
    path('', KelompokList.as_view()),
    path('<int:nomor>/', KelompokDetail.as_view()),
    path('<int:nomor>/sessions/', MentoringList.as_view()),
    path('<int:nomor>/sessions/<str:id>/', MentoringDetail.as_view()),
]