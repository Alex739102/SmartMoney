from django import forms


from .models import Transaction, Category
from django.utils import timezone


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'is_income']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introdu numele categoriei'})},

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name.strip()) < 3:
            raise forms.ValidationError("Numele categoriei trebuie să aibă cel puțin 3 caractere.")
        if name.isdigit():
            raise forms.ValidationError("Numele categoriei nu poate conține doar cifre.")
        return name

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['category', 'amount', 'date', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        amount = cleaned_data.get('amount')
        date = cleaned_data.get('date')


        if amount is not None and amount <= 0:
            self.add_error('amount', 'Suma trebuie să fie un număr pozitiv.')


        if date is not None and date > timezone.now().date():
            self.add_error('date', 'Data nu poate fi în viitor.')

        return cleaned_data

class TransactionUpdateForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['category', 'amount', 'date', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


