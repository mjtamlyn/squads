import datetime

from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from .forms import ScoreForm, SessionLogForm
from .models import Score, SessionLog, Squad, User


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        last_week = datetime.date.today() - datetime.timedelta(days=7)
        context['sessions'] = SessionLog.objects.filter(user=self.request.user
                ).filter(date__gt=last_week).order_by('-date')
        context['scores'] = Score.objects.filter(user=self.request.user).order_by('-date')[:5]
        return context


class SquadList(LoginRequiredMixin, ListView):
    model = Squad
    template_name = 'squads.html'


class SessionList(LoginRequiredMixin, ListView):
    model = SessionLog
    template_name = 'session_list.html'

    def get_queryset(self):
        return SessionLog.objects.filter(user=self.request.user).order_by('-date')


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


class SessionEdit(LoginRequiredMixin, UpdateView):
    model = SessionLog
    form_class = SessionLogForm
    template_name = 'session_form.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return SessionLog.objects.filter(user=self.request.user).order_by('-date')


class SessionDelete(LoginRequiredMixin, DeleteView):
    model = SessionLog
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return SessionLog.objects.filter(user=self.request.user).order_by('-date')


class ScoreList(LoginRequiredMixin, ListView):
    model = Score
    template_name = 'score_list.html'

    def get_queryset(self):
        return Score.objects.filter(user=self.request.user).order_by('-date')


class ScoreAdd(LoginRequiredMixin, CreateView):
    model = Score
    form_class = ScoreForm
    template_name = 'score_form.html'
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super(ScoreAdd, self).get_form_kwargs()
        kwargs['instance'] = Score(
            user=self.request.user,
            date=datetime.date.today(),
        )
        return kwargs


class ScoreEdit(LoginRequiredMixin, UpdateView):
    model = Score
    form_class = ScoreForm
    template_name = 'score_form.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Score.objects.filter(user=self.request.user).order_by('-date')


class ScoreDelete(LoginRequiredMixin, DeleteView):
    model = Score
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Score.objects.filter(user=self.request.user).order_by('-date')


class UserHistory(LoginRequiredMixin, StaffuserRequiredMixin, DetailView):
    model = User
    template_name = 'history.html'

    def get_context_data(self, **kwargs):
        context = super(UserHistory, self).get_context_data(**kwargs)
        context['squad'] = context['user'].squad
        return context
