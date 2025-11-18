
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path("routine/", views.routine),
    path('add/', views.addEmployee),
]
