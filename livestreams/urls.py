from django.urls import path
from livestreams import views

urlpatterns = [
    path("create/", views.LivestreamCreateView.as_view(), name="livestream_create"),
    path(
        "public/<uuid:public_id>/",
        views.LivestreamPublicView.as_view(),
        name="public_livestream_share",
    ),
    path("", views.LivestreamListView.as_view(), name='livestream_list'),
    path("<int:pk>", views.LivestreamDetailView.as_view(), name='livestream_detail'),
    path("complete/", views.LivestreamCompleteListView.as_view(), name='livestream_complete_list'),
    path("<int:pk>/delete/", views.LivestreamDeleteView.as_view(), name='livestream_delete'),
    path("<int:pk>/update/", views.LivestreamUpdateView.as_view(), name='livestream_update'),
]
