from django import forms
from .models import MobileDevice

class MobileDeviceForm(forms.ModelForm):
    class Meta:
        model = MobileDevice
        fields = ['brand', 'model', 'price', 'image']
