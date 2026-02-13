from django.urls import path

from Historial.views import RegisterUserView

urlpatterns = [

    path('RegisterUsers/', RegisterUserView.as_view()),
]