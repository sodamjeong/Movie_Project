from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):
    profile_image = forms.ImageField(
        label='프로필 사진',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
            }
        ),
        required=False,
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'last_name', 'birthday', 'password1', 'password2', 'profile_image', )

class CustomUserChangeForm(UserChangeForm):

    
    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('email', 'last_name', 'birthday', )