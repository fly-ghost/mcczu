from django import forms


class PlateAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='简介', required=False)


class PlatePostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='文章摘要', required=False)
