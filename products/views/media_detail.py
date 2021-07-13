from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from products.models import MediaProduct


class MediaProductDetailView(LoginRequiredMixin, DetailView):
    model = MediaProduct
    template_name = "products/media_detail.html"
    context_object_name = "media_product"
