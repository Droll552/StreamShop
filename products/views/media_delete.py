from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from products.models import MediaProduct


class MediaProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MediaProduct
    template_name = "products/media_delete.html"
    context_object_name = "media_product"
    success_url = reverse_lazy("product_list")

    def test_func(self):
        return self.get_object().user == self.request.user
