from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home-page'),
    path('search/', views.search, name='search-page'),
    path('films/', views.FilmListView.as_view(), name='films-page'),
    path('serials/', views.SerialsListView.as_view(), name='serials-page'),
    path('films/<int:pk>', views.MoviePageListView.as_view(), name='single-page'),
    path('serials/<int:pk>', views.SerialPageListView.as_view(), name='single_ser-page'),
    path('rating/', views.rating_mov, name='rating-page'),
    path("films/review/<int:pk>/", views.AddReview.as_view(), name="film_add_review"),
    path("serials/review/<int:pk>/", views.AddReview.as_view(), name="serial_add_review"),
]
