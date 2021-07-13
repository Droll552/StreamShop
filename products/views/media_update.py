from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from products.models import MediaProduct
from products.forms import MediaForm


class MediaProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = MediaForm
    model = MediaProduct
    template_name = "products/media_update.html"

    def test_func(self):
        return self.get_object().user == self.request.user

    def get_success_url(self):
        return reverse_lazy("media_detail", args=[self.get_object().pk])
