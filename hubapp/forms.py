# forms.py
from django import forms
from .models import Registration
from django.core.exceptions import ValidationError

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'email','address', 'phone', 'ssn', 
        'id_front', 'id_back', 'w2_form','idme_consent','accept','rejected']
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'firstName',
                'required': True,
                'autocomplete': 'given-name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'lastName',
                'required': True,
                'autocomplete': 'family-name'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'Email',
                'required': True,
                'autocomplete': 'email-address'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'address',
                'required': True,
                'autocomplete': 'street-address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'phone',
                'type': 'tel',
                'required': True,
                'autocomplete': 'tel'
            }),
            'ssn': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'ssn',
                'maxlength': '11',
                'placeholder': 'XXX-XX-XXXX',
                'required': True,
                'autocomplete': 'off'
            }),
            'id_front': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'idFront',
                'accept': 'image/*,.pdf',
                'required': True
            }),
            'id_back': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'idBack',
                'accept': 'image/*,.pdf',
                'required': True
            }),
            'w2_form': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'w2form',
                'accept': 'application/pdf,image/*',
                'required': True
            }),
            'idme_consent': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'idmeConsent',
                'required': True
            }),

        }
        
        labels = {
            'first_name': 'First name:',
            'last_name': 'Last name:',
            'email': 'Email:',
            'address': 'Address:',
            'phone': 'Phone No:',
            'ssn': 'SSN:',
            'id_front': 'Upload a government / valid ID (Front, all edges must show):',
            'id_back': 'Upload a government / valid ID (Back, all edges must show):',
            'w2_form': 'W2 Form — Upload:', 
            'idme_consent': 'I agree to undergo ID.me verification as part of the registration/application process. I understand that this may involve providing personal identification documents and/or biometric data.',
        }


    def clean_email(self):
        """Validate email uniqueness"""
        email = self.cleaned_data.get('email')
        if email:
            if Registration.objects.filter(email=email).exists():
                raise ValidationError("This email address has been registered.")
        return email
    
    def clean_phone(self):
        """Validate phone uniqueness"""
        phone = self.cleaned_data.get('phone')
        if phone:
            if Registration.objects.filter(phone=phone).exists():
                raise ValidationError(f"This digit '{phone}'  already exist. Use a different phone number.",)
        return phone
    
    def clean_ssn(self):
        """Validate SSN format"""
        ssn = self.cleaned_data.get('ssn')
        if ssn:
            # Remove any existing dashes and add them back
            ssn = ssn.replace('-', '')
            if len(ssn) != 9:
                raise ValidationError("SSN must be 9 digits.")
            # Format as XXX-XX-XXXX
            formatted_ssn = f"{ssn[:3]}-{ssn[3:5]}-{ssn[5:]}"
            return formatted_ssn
        return ssn