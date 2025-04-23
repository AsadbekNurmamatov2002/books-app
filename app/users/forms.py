# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.validators import validate_email

User = get_user_model()

class CreationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': _("Kiritilgan parollar bir-biriga mos kelmadi."),
        'password_too_similar': _("Parol foydalanuvchi nomiga juda o'xshash. Boshqa parol tanlang."),
        'password_too_short': _("Parol juda qisqa. Kamida 8 ta belgidan iborat bo'lishi kerak."),
        'password_common': _("Parol juda oddiy va xavfsiz emas."),
        'username_exists': _("Bu foydalanuvchi nomi band. Boshqa nom tanlang."),
        'email_exists': _("Bu elektron pochta manzili allaqachon ro'yxatdan o'tgan."),
        'invalid_email': _("Iltimos, to'g'ri elektron pochta manzilini kiriting."),
    }

    email = forms.EmailField(
        label=_("Elektron pochta"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                self.error_messages['username_exists'],
                code='username_exists',
            )
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validate_email(email)
        except forms.ValidationError:
            raise forms.ValidationError(
                self.error_messages['invalid_email'],
                code='invalid_email',
            )
            
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                self.error_messages['email_exists'],
                code='email_exists',
            )
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        username = cleaned_data.get("username")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        
        # if password1 and username and password1.lower() == username.lower():
        #     raise forms.ValidationError(
        #         self.error_messages['password_too_similar'],
        #         code='password_too_similar',
        #     )
            
        if password1 and len(password1) < 8:
            raise forms.ValidationError(
                self.error_messages['password_too_short'],
                code='password_too_short',
            )
        
        return cleaned_data