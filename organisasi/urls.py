from django.urls import path
from .views import *

urlpatterns = [
    path('', BidangList.as_view()),
    path('<str:id>/', BidangDetail.as_view()),
    path('<str:bidang_id>/sessions/', RapatList.as_view()),
    path('<str:bidang_id>/sessions/<str:id>/', RapatDetail.as_view()),
]