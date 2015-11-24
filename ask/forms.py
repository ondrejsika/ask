from django import forms

from ask.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'email',
            'bank_account',
        )

