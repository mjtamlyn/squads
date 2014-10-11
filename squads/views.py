from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin

from .models import Score, SessionLog


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['sessions'] = SessionLog.objects.filter(user=self.request.user).order_by('-date')
        context['scores'] = Score.objects.filter(user=self.request.user).order_by('-date')
        return context
