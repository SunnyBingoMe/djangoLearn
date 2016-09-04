from django import forms


class MediaForm(forms.Form):
    filename = forms.FileField(
        label='Select a file'
    )
