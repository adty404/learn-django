from django import forms


class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your email')

# example with a ModelForm
# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Participant
#         fields = ['email']
