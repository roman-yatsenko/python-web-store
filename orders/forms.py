from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'city']
        labels = {
            'first_name': _("First Name"), 
            'last_name': _("Last Name"), 
            'email': "e-mail", 
            'address': _("Address"), 
            'city': _("City"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"placeholder": field.label, 'class': 'w-75'})
            