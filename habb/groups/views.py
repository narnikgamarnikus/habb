from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Group


class GroupDetailView(LoginRequiredMixin, DetailView):
    model = Group
    # These next two lines tell the view to index lookups by Groupname


class GroupRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('groups:detail',
                       kwargs={'pk': self.kwargs['pk']})


class GroupUpdateView(LoginRequiredMixin, UpdateView):

    #fields = ['name', ]

    # we already imported Group in the view code above, remember?
    model = Group

    # send the Group back to their own page after a successful update
    def get_success_url(self):
        return reverse('groups:detail',
                       kwargs={'pk': self.kwargs['pk']})

    def get_object(self):
        # Only get the Group record for the Group making the request
        return Group.objects.get(pk=self.kwargs['pk'])


class GroupListView(LoginRequiredMixin, ListView):
    model = Group
