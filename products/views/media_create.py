from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import CreateView

from products.models import MediaProduct, Product
from products.forms import MediaForm


class MediaProductCreateView(LoginRequiredMixin, CreateView):
    form_class = MediaForm
    model = MediaProduct
    template_name = "products/media_create.html"
    success_url = reverse_lazy("product_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.product_type = Product.ProductTypeChoices.MEDIA

        return super().form_valid(form)
