from django.urls import path
from . import views
urlpatterns = [
    path('k/', views.home , name = "home"),
    path('home/<name>', views.hellothere, name = "hellothere"),
]