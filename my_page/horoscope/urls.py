from django.urls import path
from . import views


urlpatterns = [
    path('<sign_zodiac>', views.leo),
    path('scorpio/', views.scorpio),
    path('scorpio/', views.scorpio),

]