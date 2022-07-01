from cProfile import label
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Skill, Message


class CustomUserCreationForm(UserCreationForm):
    class Meta:  # metaclass defines the behavior of certain classes and their instances
        model = User
        fields = [
            "first_name",
            "email",
            "username",
            "password1",  # in django documentation
            "password2",
        ]
        labels = {"first_name": "Name"}

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update(
                {"class": "input"}
            )  # to change style of form fields (login_register, register section)
            # it's already defined in our themes


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            "name",
            "username",
            "location",
            "email",
            "short_intro",
            "bio",
            "profile_image",
            "social_github",
            "social_twitter",
            "social_linkedin",
            "social_youtube",
            "social_website",
        ]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"
        exclude = ["owner"]

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["name", "email", "subject", "body"]
        labels = {
            "name": "From",
            "email": "Your email",
            "subject": "Subject",
            "body": "Body",
        }

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})
