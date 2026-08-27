from django import forms
from .models import DesignOrder


class DesignOrderForm(forms.ModelForm):
    class Meta:
        model = DesignOrder
        fields = [
            'service',
            'title',
            'description',
        ]
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'rows': 5,
                    'placeholder': 'Describe what you would like designed.'
                }
            ),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if len(title.strip()) < 3:
            raise forms.ValidationError(
                'Please enter a title with at least 3 characters.'
            )

        return title