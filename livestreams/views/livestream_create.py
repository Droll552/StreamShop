from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from livestreams.models import Livestream
from livestreams.forms import LivestreamCreateForm


class LivestreamCreateView(LoginRequiredMixin, CreateView):
    form_class = LivestreamCreateForm
    model = Livestream
    template_name = "livestreams/livestream_create.html"
    success_url = reverse_lazy("livestream_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
