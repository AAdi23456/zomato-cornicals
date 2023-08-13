from django.urls import path
from . import views

urlpatterns = [
    path("adddish/", views.add_dish),
    path("updatedish/", views.updatedish),
    path("deletedish/", views.Delete_data),
    path("getdish/", views.Get_data),
    path("addorder/", views.add_order),
    path("updateorder/", views.update_order),
    path("fetchorder/", views.fetch_orders),
]
