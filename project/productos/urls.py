from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "productos"

urlpatterns = [
    path("", TemplateView.as_view(template_name="producto/index"), name="index"),
    path("productocategoria/list/", views.ProductoCategoriaList.as_view(), name="productocategoria_list"),
    path("productocategoria/detail/<int:pk>", views.ProductoCategoriaDetail.as_view(), name="productocategoria_detail"),
    #path("comprar/", views.comprar, name="comprar"),
]

urlpatterns += staticfiles_urlpatterns()