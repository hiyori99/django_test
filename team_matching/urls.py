from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("brian", views.brian, name="brain"),
  path("<str:name>", views.greet, name="greet"),
]