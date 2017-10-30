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


class WidgetJSDetailView(LoginRequiredMixin, DetailView):
    model = Widget 
    slug_field = 'token'
    slug_url_kwarg = 'token'
    template_name = 'widgets/widget_detail.js'
    content_type = 'application/javascript'

    def get_context_data(self, *args, **kwargs):
        context = super(WidgetJSDetailView, self).get_context_data(*args, **kwargs)
        self.object.website.user.generate_token()
        context['user_token'] = self.object.website.user.encode_user_token()
        context['opened'] = self.object.opened + 1
        context['closed'] = self.object.closed + 1
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.viewed += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class WidgetHTMLDetailView(LoginRequiredMixin, DetailView):
    model = Widget 
    slug_field = 'token'
    slug_url_kwarg = 'token'
    template_name = 'widgets/widget_base.html'
    #content_type = 'application/javascript'

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
from rest_framework import mixins
from rest_framework import generics


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response




class APIWidgetView(mixins.RetrieveModelMixin,
                    #mixins.UpdateModelMixin,
                    generics.GenericAPIView):
    
    #queryset = Widget.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Widget.objects.filter(website__user=user)
        #return Leed.objects.filter(widget__user=user)

    serializer_class = WidgetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

'''
class APIWidgetOpenedView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    generics.GenericAPIView):


class APIWidgetClosedView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    generics.GenericAPIView):


class APIWidgetViewedView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    generics.GenericAPIView):
'''
    #def post(self, request, *args, **kwargs):
    #    return self.create(request, *args, **kwargs)
'''
class LeedList(APIView):

    def post(self, request, format=None):
        serializer = LeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

class APILeedListView(mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):

    #queryset = Leed.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Leed.objects.filter(widget__website__user=user)

    serializer_class = LeedSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class APILeedDetailView(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,                    
                        generics.GenericAPIView):

    queryset = Leed.objects.all()

    #def get_queryset(self):
    #    user = self.request.user
    #    return Leed.objects.filter(widget__website__user=user)

    serializer_class = LeedSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)





@api_view(['PUT'])
def widget_opened(request, pk):

    try:
        widget = Widget.objects.get(pk=pk)
        widget.opened += 1
        widget.save()
    except Widget.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_200_OK)


@api_view(['PUT'])
def widget_closed(request, pk):

    try:
        widget = Widget.objects.get(pk=pk)
        widget.closed += 1
        widget.save()
    except Widget.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_200_OK)


@api_view(['PUT'])
def widget_viewed(request, pk):

    try:
        widget = Widget.objects.get(pk=pk)
        widget.viewed += 1
        widget.save()
    except Widget.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_200_OK)