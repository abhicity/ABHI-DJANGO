from django import forms
from .models import BlogModel


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ["title", "content", "publish", "dop"]
        # fields = "__all__"
        # exclude = "dop"


class ContactForm(forms.Form):
    name = forms.CharField(max_length=10, required=False, help_text="Enter the Name")
    email = forms.EmailField()
    dop = forms.DateField()

    class Meta:
        fields = ["name", "email"]
