from django.urls import path
from hello import views

urlpatterns = [
    path(" test/", views.append_to_file, name="append_to_file"),
]
