from django import forms
from .models import Item, Category

NORMAL_CLASS = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"


class AddItemForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': NORMAL_CLASS, 'id': 'name'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': NORMAL_CLASS, 'id': 'price'}))
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': NORMAL_CLASS, 'id': 'category'})
    )
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'hidden', 'id': 'image'}), required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'}))

    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')


class EditItemForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': NORMAL_CLASS, 'id': 'name'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': NORMAL_CLASS, 'id': 'price'}))
    status = forms.BooleanField(widget=forms.CheckboxInput(attrs={'id': 'status'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'hidden', 'id': 'image'}), required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}))

    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
