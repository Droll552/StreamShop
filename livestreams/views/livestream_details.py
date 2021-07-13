from livestreams.models import Livestream

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView


class LivestreamDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Livestream
    template_name = 'livestreams/livestream_details.html'
    context_object_name = 'livestream'

    def test_func(self):
        object = self.get_object()
        return object.user == self.request.user

