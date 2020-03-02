from django import forms


class DepartmentAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='简介', required=True)


class DepartmentPostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='文章摘要', required=False)
