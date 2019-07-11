from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse
from .models import LogItem

# Create your views here.
class LogList(ListView):
  model = LogItem
  ordering = ['-id']
  paginate_by = 1

class LogView(DetailView):
  model = LogItem

class LogCreate(CreateView):
  model = LogItem
  fields = ['subject', 'description', 'reporter', 'phone']

  def get_success_url(self):
    return reverse('log_list')

class LogReply(UpdateView):
  model = LogItem
  fields = ['handler', 'status', 'comment']

  def get_success_url(self):
    return reverse('log_view', self.object.id)