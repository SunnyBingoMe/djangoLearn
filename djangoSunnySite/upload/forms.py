from django import forms


class MediaForm(forms.Form):
    filename = forms.FileField(
        label='Select a file'
    )


class FileFieldForm(forms.Form):
    multi_file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
