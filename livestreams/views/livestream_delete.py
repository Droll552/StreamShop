from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from livestreams.models import Livestream


class LivestreamDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Livestream
    template_name = "livestreams/livestream_delete.html"
    success_url = reverse_lazy("livestream_list")

    def test_func(self):
        return self.get_object().user == self.request.user
