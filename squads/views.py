import datetime

from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from .forms import ScoreForm, SessionLogForm, CoachNoteForm, VideoForm
from .models import TrainingCategory, Score, SessionLog, Squad, User, CoachNote, Video


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        last_week = datetime.date.today() - datetime.timedelta(days=7)
        context['sessions'] = SessionLog.objects.filter(user=self.request.user
                ).filter(date__gt=last_week).order_by('-date')
        context['scores'] = Score.objects.filter(user=self.request.user).order_by('-date')[:5]
        context['videos'] = Video.objects.filter(subject=self.request.user).order_by('-date')[:3]
        return context


class Information(LoginRequiredMixin, ListView):
    template_name = 'information.html'

    def get_queryset(self):
        return TrainingCategory.objects.prefetch_related('trainingtype_set')


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


class VideoList(LoginRequiredMixin, ListView):
    model = Video
    template_name = 'score_list.html'

    def get_queryset(self):
        return Video.objects.filter(subject=self.request.user).order_by('-date')


class VideoAdd(LoginRequiredMixin, CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'score_form.html'
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super(VideoAdd, self).get_form_kwargs()
        kwargs['instance'] = Video(
            subject=self.request.user,
            date=datetime.date.today(),
        )
        return kwargs


class VideoEdit(LoginRequiredMixin, UpdateView):
    model = Video
    form_class = VideoForm
    template_name = 'score_form.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Video.objects.filter(subject=self.request.user).order_by('-date')


class VideoDelete(LoginRequiredMixin, DeleteView):
    model = Video
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Video.objects.filter(subject=self.request.user).order_by('-date')


class UserHistory(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'history.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            return super(UserHistory, self).dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return redirect_to_login(request.get_full_path(),
                    self.get_login_url(),
                    self.get_redirect_field_name())

    def get_object(self):
        user = super(UserHistory, self).get_object()
        if not self.request.user.is_staff and not user.public_profile:
            raise PermissionDenied
        return user

    def get_context_data(self, **kwargs):
        context = super(UserHistory, self).get_context_data(**kwargs)
        context['squad'] = context['user'].squad
        context['coach_mode'] = self.request.user.is_staff
        if context['coach_mode']:
            context['archers'] = User.objects.filter(squad=self.object.squad)
        else:
            context['archers'] = User.objects.filter(public_profile=True)
        return context


class CoachNoteAdd(LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
    model = CoachNote
    form_class = CoachNoteForm
    template_name = 'note_form.html'

    def get_success_url(self):
        return reverse('user-history', kwargs=self.kwargs)

    def get_archer(self):
        return get_object_or_404(User, pk=self.kwargs['pk'])

    def get_form_kwargs(self):
        kwargs = super(CoachNoteAdd, self).get_form_kwargs()
        kwargs['instance'] = CoachNote(
            author=self.request.user,
            subject=self.get_archer(),
            timestamp=timezone.now(),
        )
        return kwargs
