from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from sweet_dating import settings
from sweet_dating_app.models import Portfolio


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "first_name", "last_name")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            self._meta.model._default_manager.get(username=username)
        except self._meta.model.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def save(self, commit=True):
        user = super(EmailUserCreationForm, self).save(commit=commit)
        text_content = 'Thank you for signing up for our website at {}, {} {}'\
            .format(user.date_joined, user.first_name, user.last_name)
        html_content = '<h2>Thanks {} {} for signing up at {}!</h2> <div>I hope you enjoy using our site</div>'\
            .format(user.first_name, user.last_name, user.date_joined)
        msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return user


class PortfolioForm(forms.ModelForm):
    gender_choice = (
        ('M', "Male"),
        ('F', "Female"),
        ('O', "Others")
    )

    gender = forms.ChoiceField(choices=gender_choice)
    age = forms.IntegerField()
    target_gender = forms.ChoiceField(choices=gender_choice)

    class Meta:
        model = Portfolio
        fields = ("gender", "age", "user_photo", "target_gender")