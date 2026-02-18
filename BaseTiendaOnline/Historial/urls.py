from django.urls import path

from Historial.views import RegisterUserView, LoginView

urlpatterns = [

    path('RegisterUsers/', RegisterUserView.as_view()),
    path('LoginUsers/', LoginView.as_view()),
]