from django import forms
from django.contrib.auth import models as auth
from django.forms.models import modelformset_factory, inlineformset_factory

from qualitio.projects import models
from qualitio import store
from qualitio import execute
from qualitio import glossary
from qualitio.core import forms as core


class OrganizationProfileForm(core.BaseModelForm):

    class Meta(core.BaseModelForm.Meta):
        model = models.Organization
        fields = ("name", "slug", "homepage", "description", "googleapps_domain")
        widgets = {
            'name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'slug': forms.TextInput(attrs={'readonly': 'readonly'})
        }


class OrganizationMemberForm(core.BaseModelForm):

    class Meta(core.BaseModelForm.Meta):
        model = models.OrganizationMember
        fields = ("role",)


class ProjectForm(core.BaseModelForm):

    class Meta(core.BaseModelForm.Meta):
        model = models.Project
        fields = ("name", "homepage", "description")


class ProjectUserForm(core.BaseForm):
    username = forms.CharField()

    def clean_username(self):
        data = self.cleaned_data['username']

        try:
            user = auth.User.objects.get(username=data)
        except auth.User.DoesNotExist:
            raise forms.ValidationError("User does not exist.")

        return data


OrganizationUsersForm = modelformset_factory(models.OrganizationMember,
                                             form=OrganizationMemberForm,
                                             formset=core.BaseModelFormSet,
                                             extra=0, can_delete=True)

OrganizationProjectsForm = modelformset_factory(models.Project,
                                                form=ProjectForm,
                                                formset=core.BaseModelFormSet,
                                                extra=0, can_delete=False)

ProjectTestCaseStatusFormSet = inlineformset_factory(models.Project,
                                                     store.TestCaseStatus,
                                                     formset=core.BaseInlineFormSet,
                                                     extra=0)

ProjectTestRunStatusFormSet = inlineformset_factory(models.Project,
                                                    execute.TestRunStatus,
                                                    formset=core.BaseInlineFormSet,
                                                    extra=0)

ProjectTestCaseRunStatusFormSet = inlineformset_factory(models.Project,
                                                        execute.TestCaseRunStatus,
                                                        formset=core.BaseInlineFormSet,
                                                        extra=0)

ProjectGlossaryLanguageFormSet = inlineformset_factory(models.Project,
                                                       glossary.Language,
                                                       formset=core.BaseInlineFormSet,
                                                       extra=0)
