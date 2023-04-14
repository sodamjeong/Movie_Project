from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django import forms

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        label=("비밀번호"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': False,
                'class': 'form-control',
            }
        ),
    )
    


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': False,
            }
        )
    )
    email = forms.EmailField(
        label='이메일',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    last_name = forms.CharField(
        label='성명',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    birthday = forms.DateField(
        label='생년월일',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
            }
        )
    )
    password1 = forms.CharField(
        label='비밀번호',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'autocomplete': False,
            }
        )
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'autocomplete': False,
            }
        )
    )
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
    email = forms.EmailField(
        label='이메일',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    last_name = forms.CharField(
        label='성명',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    birthday = forms.DateField(
        label='생년월일',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
            }
        )
    )
    profile_image = forms.ImageField(
        label='프로필 사진',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
            }
        ),
        required=False,
    )

    password = None
    
    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('email', 'last_name', 'birthday', 'profile_image', )


class CustomPasswordChangeForm(PasswordChangeForm):
    new_password1 = forms.CharField(
        label='새 비밀번호',
        widget= forms.PasswordInput(),
        help_text='',
    )