from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from products.models import Product


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        return self.request.user.products.all()
