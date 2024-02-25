from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="home"),
    path('index.html',views.index, name="index"),
    path("portfolio-details.html",views.portfolio, name="portfolio"),
    path("portfolio-details2.html",views.portfolio2, name="portfolio"),
     path("portfolio-details3.html",views.portfolio3, name="portfolio"),
]
#This is special url path for handling errors
handler404 = "website.views.error_404_view"