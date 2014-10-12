import datetime

from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, CreateView

from braces.views import LoginRequiredMixin

from .forms import SessionLogForm
from .models import Score, SessionLog


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['sessions'] = SessionLog.objects.filter(user=self.request.user).order_by('-date')
        context['scores'] = Score.objects.filter(user=self.request.user).order_by('-date')
        return context


class SessionAdd(LoginRequiredMixin, CreateView):
    model = SessionLog
    form_class = SessionLogForm
    template_name = 'session_form.html'
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super(SessionAdd, self).get_form_kwargs()
        kwargs['instance'] = SessionLog(
            user=self.request.user,
            date=datetime.date.today(),
        )
        return kwargs
