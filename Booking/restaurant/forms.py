import forms
from models import *

class BookingForm (forms.ModelForm):
    class Meta():
        Model = Booking
        Field = '__all__'
        
