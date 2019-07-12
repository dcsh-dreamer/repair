from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import LogItem
from .forms import LogItemReplyForm

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

class LogReply(LoginRequiredMixin, UpdateView):
  model = LogItem
  #fields = ['handler', 'status', 'comment']
  form_class = LogItemReplyForm
  template_name = 'log/logitem_detail.html'

  def get_success_url(self):
    return reverse('log_view', kwargs={'pk': self.object.id})
  
  # get_initial: 設定表單初始預設值
  def get_initial(self):
    data = {}
    # 取得目前登入的使用者資訊
    u = self.request.user
    # 如果有名字，就填名字，否則就填帳號名稱
    if u.first_name:
      data['handler'] = u.first_name
    else:
      data['handler'] = u.username
    return data