from django.urls import path

from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("view-novel/<int:novel_id>", views.view_novel, name="viewnovel"),
    path("pricing", views.view_pricing, name="pricing"),

    #API URL
    path("<int:country_id>/get-towns", views.get_town, name="towns"),
    path("<int:town_id>/get-categories", views.get_categories, name="categories"),
    path('<int:country_id>/<int:town_id>/<int:category_id>/get-novels', views.get_novels, name='get-novels'),
    path("api/get-countries", views.get_countries, name="allcountries"),
    path("api/get-towns/<int:country_id>", views.get_towns_api, name="alltowns"),
    path("api/get-categories/<int:town_id>", views.get_categories_api, name="allcategories"),
    path("api/get-novels/<int:country_id>/<int:town_id>/<int:category_id>", views.get_novels_api, name="allnovelapi"),
]