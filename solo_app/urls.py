from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    #path('profile', views.profile),
    path('login', views.login),
    path('logout', views.logout),
    path('main', views.main_page),
    path('make_post', views.make_post),
    path('main/<int:id>/delete', views.delete),
    path('like/<int:id>', views.add_like),
    path('main/<int:id>/edit', views.edit),
    path('main/<int:id>/update', views.update),
    path('back', views.back),
    path('main/<int:id>/show', views.show_post),
    path('welcome', views.welcome),
]