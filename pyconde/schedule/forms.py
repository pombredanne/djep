# -*- encoding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit

from . import models


class EditSessionForm(forms.ModelForm):
    class Meta(object):
        model = models.Session
        fields = ['description', 'abstract']

    def __init__(self, *args, **kwargs):
        super(EditSessionForm, self).__init__(*args, **kwargs)
        self.fields['description'].label = ugettext("Description")
        self.fields['abstract'].label = ugettext("Abstract")
        self.fields['abstract'].help_text = ugettext("""This field supports <a href="http://daringfireball.net/projects/markdown/syntax" target="_blank" rel="external">Markdown</a> as input.""")
        self.fields['description'].help_text = ugettext("""This field supports <a href="http://daringfireball.net/projects/markdown/syntax" target="_blank" rel="external">Markdown</a> as input.""")
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Field('description'),
            Field('abstract'),
            ButtonHolder(Submit('save', _("Save"), css_class="btn btn-primary"))
            )
