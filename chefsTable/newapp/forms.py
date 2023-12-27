from django import forms    

SHIFTS = (
    ("1", "Morning"),
    ("2", "Afternoon"),
    ("3", "Evening"),
)


class InputForm(forms.Form): 
    first_name = forms.CharField(label='Firt Name', max_length=50) 
    last_name = forms.CharField(label='Last Name', max_length=50) 
    shift = forms.ChoiceField(choices = SHIFTS)
    time_log = forms.TimeField()

    # address = forms.CharField(label='Address', max_length=100) 
    # posts = (('Manager', 'Manager'),('Cashier', 'Cashier'),('Operator', 'Operator')) 
    # field = forms.ChoiceField(choices=posts) 