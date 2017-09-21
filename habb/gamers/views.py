from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Gamer


class GamerDetailView(LoginRequiredMixin, DetailView):
    model = Gamer
    # These next two lines tell the view to index lookups by Gamename
    

class GamerRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('games:detail',
                       kwargs={'pk': self.kwargs['pk']})


class GamerUpdateView(LoginRequiredMixin, UpdateView):

    #fields = ['name', ]

    # we already imported Game in the view code above, remember?
    model = Gamer

    # send the Game back to their own page after a successful update
    def get_success_url(self):
        return reverse('games:detail',
                       kwargs={'pk': self.kwargs['pk']})

    def get_object(self):
        # Only get the Game record for the Game making the request
        return Gamer.objects.get(pk=self.kwargs['pk'])


class GamerListView(LoginRequiredMixin, ListView):
    model = Gamer
