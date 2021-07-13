from livestreams.models import Livestream

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView


class LivestreamCompleteListView(LoginRequiredMixin, ListView):
    model = Livestream
    template_name = "livestreams/complete_livestream_list.html"
    context_object_name = "livestreams"

    def get_queryset(self):
        return Livestream.objects.complete_livestreams(self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["counted_complete"] = Livestream.objects.counted_complete(self.request.user)
        return context
