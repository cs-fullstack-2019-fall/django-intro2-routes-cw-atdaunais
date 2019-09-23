from . import views
from django.urls import path

urlpatterns = {
    path('gogetthegood/', views.goGetTheGood, name="getit"),
    path('happyhappyjoyjoy/', views.happyHappyJoyJoy, name="sister"),
    path('<str:text>/', views.acceptString, name="userinput"),
}