from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView


class AccountUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    pass