from django import forms 

class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget = forms.TextInput(
            attrs={"class":"form-control", "placeholder": "full name"}))

    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs={"class": "form-control", "placeholder":"email"}))

    content = forms.CharField(
        widget = forms.Textarea(
            attrs={"class": "form-control", "placeholder":"your message ..."}))

def clean_email(self):
    email = self.cleaned_data.get("email")
    if "gmail.com" not in email:
        raise forms.ValidationError("email has to be gmail.com")
    return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password =forms.CharField(widget=forms.PasswordInput)