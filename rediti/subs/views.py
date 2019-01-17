from django.shortcuts import render
from django.views import generic
from .models import Subred, Thread, Post
# Create your views here.
class SubredsView(generic.ListView):
    model = Subred
    template_name = 'subs/subred.html'
    context_object_name = 'subreds'

class SubredView(generic.DetailView):
    template_name = 'subs/subreds.html'
    model = Subred

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     subscription, created = Subscription.objects.get_or_create(user=self.request.user, subrediti=self.object)
    #     context['subscribed'] = True if subscription.subscribed else False
    #     return context 