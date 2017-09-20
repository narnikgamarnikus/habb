from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Team


class GroupDetailView(LoginRequiredMixin, DetailView):
    model = Team
    # These next two lines tell the view to index lookups by Groupname
    

class GroupRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('Groups:detail',
                       kwargs={'name': self.kwargs['name']})


class GroupUpdateView(LoginRequiredMixin, UpdateView):

    #fields = ['name', ]

    # we already imported Team in the view code above, remember?
    model = Team

    # send the Group back to their own page after a successful update
    def get_success_url(self):
        return reverse('Groups:detail',
                       kwargs={'name': self.kwargs['name']})

    def get_object(self):
        # Only get the Group record for the Group making the request
        return Team.objects.get(name=self.kwargs['name'])


class GroupListView(LoginRequiredMixin, ListView):
    model = Team
