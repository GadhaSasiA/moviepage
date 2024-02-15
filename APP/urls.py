from django.urls import path,include
from .views import*
from.import views


urlpatterns=[
    path('',index,name='index'),
    path('home',home,name='home'),
    path('favourites/',favourite_movies,name='favourites'),
    path('add_to_favourite/',favourite_movies, name='add_to_favourite'),
    path('login',login,name='login'),

    path('movie_times',movie_times,name='movie_times'),
    #path('add_to_favourites/<int:movie_id>/',add_to_favourites, name='add_to_favourites'),
    path('about',about,name='about'),
    path('user_login/',user_login,name='user_login'),
    path('user_register/',user_register,name='user_register'),
    path('Add',Add,name='Add'),
    path('insert/',views.insertData, name='insertData'),
    #path('search/',views.search, name='search'),
    #path('movie_search/<int:movie_id>/', views.movie_search, name='movie_search'),
    path('search_view/', search_view, name='search_view'),
    path('update/<id>',views.updateData, name='updateData'),
    path('delete/<id>',views.deleteData, name='deleteData'),


]