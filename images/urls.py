from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('category/<slug:slug>/',views.category_detail,name='category_detail'),
    path('image/<int:pk>/',views.image_detail,name='image_detail'),
    path('search/',views.search,name='search'),
]
