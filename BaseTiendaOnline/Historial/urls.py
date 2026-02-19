from django.urls import path

from Historial.views import RegisterUserView, LoginView, CitasView

urlpatterns = [

    path('RegisterUsers/', RegisterUserView.as_view()),
    path('LoginUsers/', LoginView.as_view()),
    path('Citas/', CitasView.as_view()),
]