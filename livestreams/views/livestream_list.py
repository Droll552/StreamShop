from livestreams.models import Livestream

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView


class LivestreamListView(LoginRequiredMixin, ListView):
    model = Livestream
    template_name = "livestreams/livestream_list.html"
    context_object_name = "livestreams"

    def get_queryset(self):
        return Livestream.objects.hosted_by(self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["upcoming_livestreams"] = Livestream.objects.upcoming_livestreams(self.request.user)
        context["in_progress_livestreams"] = Livestream.objects.in_progress_livestreams(self.request.user)
        context["in_payment_request"] = Livestream.objects.in_payment_request(self.request.user)

        context["counted_upcoming"] = Livestream.objects.counted_upcoming(self.request.user)
        context["counted_in_progress"] = Livestream.objects.counted_in_progress(self.request.user)
        context["counted_in_payment"] = Livestream.objects.counted_in_payment(self.request.user)
        return context

