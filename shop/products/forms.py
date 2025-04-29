from django import forms


class ProductSearchForm(forms.Form):
    search_field = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'search-form',
        'placeholder': 'Найти',
    }))