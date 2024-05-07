from django.forms import ModelForm
import .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields=('name', 'email', 'subject', 'message')