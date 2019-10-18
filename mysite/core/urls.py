from django.conf.urls import url, include
from . import views

urlpatterns = [
        url('^ponto/new', views.add_new_point_view, name="add_new_point"),
]