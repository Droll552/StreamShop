from django.db import models


class LivestreamManager(models.Manager):
    def hosted_by(self, user):
        return self.filter(user=user)

    def counted_upcoming(self, user):
        return self.upcoming_livestreams(user).count()

    def counted_in_progress(self, user):
        return self.in_progress_livestreams(user).count()

    def counted_in_payment(self, user):
        return self.in_payment_request(user).count()

    def counted_complete(self, user):
        return self.complete_livestreams(user).count()

    def allowed_to_update(self, user):
        upcoming_livestreams = self.upcoming_livestreams(user)
        in_progress_livestreams = self.in_progress_livestreams(user)

        return upcoming_livestreams | in_progress_livestreams

    def upcoming_livestreams(self, user):
        from livestreams.models import Livestream
        return self.filter(user=user, status=Livestream.StreamStatusChoices.UPCOMING)

    def in_progress_livestreams(self, user):
        from livestreams.models import Livestream
        return self.filter(user=user, status=Livestream.StreamStatusChoices.IN_PROGRESS)

    def in_payment_request(self, user):
        from livestreams.models import Livestream
        return self.filter(user=user, status=Livestream.StreamStatusChoices.IN_PAYMENT_REQUEST)

    def complete_livestreams(self, user):
        from livestreams.models import Livestream
        return self.filter(user=user, status=Livestream.StreamStatusChoices.COMPLETE_LIVESTREAMS)
