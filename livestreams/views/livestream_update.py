from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from livestreams.forms import LivestreamUpdateForm
from livestreams.models import Livestream


class LivestreamUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Livestream
    form_class = LivestreamUpdateForm
    template_name = "livestreams/livestream_update.html"
    success_url = reverse_lazy("livestream_list")

    def get_queryset(self):
        return Livestream.objects.allowed_to_update(self.request.user)

    def test_func(self):
        return self.get_object().user == self.request.user
