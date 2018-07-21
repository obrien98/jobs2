from django.forms import ModelForm, forms
from .models import Job
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import UpdateView


class EmployerSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields =  ('first_name',
                   'last_name',
                   'email',
                   'username',
                   'password1',
                   'password2',)
        help_texts = {
            'username': None,
            'password': None,
        }

class JobPostForm(ModelForm):
    class Meta:
        model = Job
        fields= ('job_title',
                 'establishment_name',
                 'details',
                 'address',
                 'city',
                 'state',
                 'zip_code',
               )

