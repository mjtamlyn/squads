from django.db import transaction
from django import forms
from django.forms.models import inlineformset_factory

from .models import SessionLog, SessionSection


class SessionSectionForm(forms.ModelForm):
    required_css_class = 'required'
    error_css_class = 'error'

    class Meta:
        model = SessionSection
        fields = ('training_type', 'time')


SessionSectionFormset = inlineformset_factory(SessionLog, SessionSection, form=SessionSectionForm)


class SessionLogForm(forms.ModelForm):
    required_css_class = 'required'
    error_css_class = 'error'

    class Meta:
        model = SessionLog
        fields = ('date', 'venue', 'arrows_shot', 'notes')

    def __init__(self, **kwargs):
        super(SessionLogForm, self).__init__(**kwargs)
        self.formset = SessionSectionFormset(**kwargs)

    def is_valid(self):
        return super(SessionLogForm, self).is_valid() and self.formset.is_valid()

    def save(self):
        with transaction.atomic():
            obj = super(SessionLogForm, self).save()
            self.formset.save()
        return obj
