from django import forms


class ProductSearchForm(forms.Form):
    search_field = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'search-form',
        'placeholder': 'Поиск',
    }))