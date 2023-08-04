from django.urls import path
from . import views

urlpatterns = [
    path("feedback/list/", views.feedback_list, name="feedback_list"),
    path("feedback/new/", views.feedback_new, name="feedback_new"),
]
