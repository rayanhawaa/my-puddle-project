from django import forms

from .models import Item

INPUT_STYLES = 'width:100%; padding-block:0.4rem; padding-inline:0.6rem; border-radius:10px; border:10px;'
class NewItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'style': INPUT_STYLES})

class EditItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'style': INPUT_STYLES})