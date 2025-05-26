from django import forms


from .models import Transaction, Category
from django.utils import timezone


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'is_income']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Insert category name'
            }),
            'is_income': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'style': 'outline: 1px solid #000; outline-offset: 1px;',
                }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name.strip()) < 3:
            raise forms.ValidationError("The name should be at least 3 characters long.")
        if name.isdigit():
            raise forms.ValidationError("The category name should not only contain numbers.")
        return name

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['category', 'amount', 'date', 'description']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Insert transaction amount'
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descrption(Optional)',
                'rows': 3,
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        amount = cleaned_data.get('amount')
        date = cleaned_data.get('date')


        if amount is not None and amount <= 0:
            self.add_error('amount', 'The amount should be greater than zero.')


        if date is not None and date > timezone.now().date():
            self.add_error('date', 'Date should not be in the future.')

        return cleaned_data

class TransactionUpdateForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['category', 'amount', 'date', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


