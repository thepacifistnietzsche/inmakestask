from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from persons.models import Person, District,Branch


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

ACCOUNT_CHOICES=[('Savings','savings'),
         ('Current','Current')]
GENDER_CHOICES=[('Male','Male'),
         ('Female','Femal')]
DOCUMENT_CHOICES=[('Aadhar','Aadhar'),
         ('PAN','PAN'),('Passport','Passport'),('DL','DL')]

class PersonCreationForm(forms.ModelForm):
    Account_type = forms.ChoiceField(choices=ACCOUNT_CHOICES, widget=forms.RadioSelect())
    Documents = forms.ChoiceField(choices=DOCUMENT_CHOICES, widget=forms.CheckboxSelectMultiple())
    Gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'country' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')
