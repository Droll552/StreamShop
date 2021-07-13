from django.views.generic import DetailView

from livestreams.models import Livestream


class LivestreamPublicView(DetailView):
    model = Livestream
    template_name = "livestreams/livestream_detail.html"
    context_object_name = "livestream"

    def get_object(self, queryset=None):
        return Livestream.objects.get(public_id=self.kwargs.get("public_id"))
