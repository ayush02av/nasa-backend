from django.urls import path
from . import views

urlpatterns = [
    path('gots/', views.gots_predict.as_view()),
]