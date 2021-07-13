from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView


class AccountDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    pass