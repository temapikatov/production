from django.urls import path
from . import views

urlpatterns = [
    path('main/',views.home_view.as_view(), name='main'),
    path('home/', views.home, name="home"),
    path('download/', views.download, name="download")
]