from django.urls import path
from products import views

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product_list"),
    path("media/<int:pk>/delete/", views.MediaProductDeleteView.as_view(), name="media_delete"),
    path("media/create/", views.MediaProductCreateView.as_view(), name="media_create"),
    path("media/<int:pk>/update/", views.MediaProductUpdateView.as_view(), name="media_update"),
    path("media/<int:pk>", views.MediaProductDetailView.as_view(), name="media_detail")
]
