from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Map


class MapDetailView(LoginRequiredMixin, DetailView):
    model = Map
    # These next two lines tell the view to index lookups by Groupname
    

class MapRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('maps:detail',
                       kwargs={'name': self.kwargs['name']})


class MapUpdateView(LoginRequiredMixin, UpdateView):

    #fields = ['name', ]

    # we already imported Map in the view code above, remember?
    model = Map

    # send the Map back to their own page after a successful update
    def get_success_url(self):
        return reverse('maps:detail',
                       kwargs={'name': self.kwargs['name']})

    def get_object(self):
        # Only get the Group record for the Group making the request
        return Map.objects.get(name=self.kwargs['name'])


class MapListView(LoginRequiredMixin, ListView):
    model = Map
