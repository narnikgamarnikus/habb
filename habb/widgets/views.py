from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Widget, Website, Leed
from .forms import WidgetForm
from django.shortcuts import get_object_or_404

class WidgetDeleteView(LoginRequiredMixin, DeleteView):
    model = Widget


class WidgetCreateView(LoginRequiredMixin, CreateView):
    model = Widget
    form_class = WidgetForm

    def form_valid(self, form):
        return super(WidgetCreateView, self).form_valid(form)


    def get_form_kwargs(self):
        kwargs = super(WidgetCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class WidgetDetailView(LoginRequiredMixin, DetailView):
    model = Widget 
    slug_field = 'token'
    slug_url_kwarg = 'token'
    template_name = 'widgets/widget_detail.js'
    content_type = 'application/javascript'

    def get_context_data(self, *args, **kwargs):
        context = super(WidgetDetailView, self).get_context_data(*args, **kwargs)
        context['user_token'] = self.object.website.user.encode_user_token()
        context['opens'] = self.self.object.opens + 1
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)



class WidgetRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('widgets:detail',
                       kwargs={'token': self.kwargs['token']})


class WidgetUpdateView(LoginRequiredMixin, UpdateView):

    model = Widget

    def get_success_url(self):
        return reverse('widgets:detail',
                       kwargs={'token': self.kwargs['token']})

    def get_object(self):
        return Widget.objects.get(token=self.kwargs['token'])


class WidgetListView(LoginRequiredMixin, ListView):
    model = Widget

    def get_queryset(self):
        queryset = super(WidgetListView, self).get_queryset()
        return queryset.filter(website__user = self.request.user)











class WebsiteDeleteView(LoginRequiredMixin, DeleteView):
    model = Website


class WebsiteCreateView(LoginRequiredMixin, CreateView):
    model = Website
    fields = ['name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WebsiteCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('widgets:website_detail',
                       kwargs={'pk': self.object.pk})


class WebsiteDetailView(LoginRequiredMixin, DetailView):
    model = Website

    def get_context_data(self, *args, **kwargs):
        context = super(WebsiteDetailView, self).get_context_data(*args, **kwargs)
        context['widgets'] = Widget.objects.filter(website = self.object)
        return context

    #def get_object(self, queryset=None):
    #    return get_object_or_404(Website, pk=self.kwargs['pk'])


class WebsiteRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('widgets:website_detail',
                       kwargs={'pk': self.kwargs['pk']})


class WebsiteUpdateView(LoginRequiredMixin, UpdateView):

    model = Website

    def get_success_url(self):
        return reverse('widgets:website_detail',
                       kwargs={'pk': self.kwargs['pk']})

    def get_object(self):
        return Website.objects.get(pk = self.kwargs['pk'])


class WebsiteListView(LoginRequiredMixin, ListView):
    model = Website

    def get_queryset(self):
        queryset = super(WebsiteListView, self).get_queryset()
        return queryset.filter(user = self.request.user)






class LeedDetailView(LoginRequiredMixin, DetailView):
    model = Leed


class LeedListView(LoginRequiredMixin, ListView):
    model = Leed

    def get_queryset(self):
        queryset = super(LeedListView, self).get_queryset()
        return queryset.filter(widget__website__user = self.request.user)














from .serializers import LeedSerializer, WidgetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LeedList(APIView):

    def get(self, request, format=None):
        leeds = Leed.objects.all()
        serializer = LeedSerializer(leeds, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WidgetList(APIView):

    def get(self, request, format=None):
        leeds = Widget.objects.all()
        serializer = WidgetSerializer(leeds, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WidgetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)