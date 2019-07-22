
from django.urls import path,include
from api import views

urlpatterns=[
   path('users/',views.stockList.as_view()),
   path('users/<int:id>/',views.stockList.as_view()),
    
]
