# from django import forms
# from .models import Product, BOMItem

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name', 'description']

# class BOMItemForm(forms.ModelForm):
#     class Meta:
#         model = BOMItem
#         fields = ['item_name', 'item_type', 'quantity', 'unit', 'price','notes']
from django import forms
from .models import Product, BOMItem

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description']

class BOMItemForm(forms.ModelForm):
    class Meta:
        model = BOMItem
        fields = ['item_name', 'item_type', 'quantity', 'unit', 'price', 'notes', 'custom_item_type']  # Add 'custom_item_type'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initially hide the 'custom_item_type' field
        self.fields['custom_item_type'].widget.attrs['style'] = 'display: none;'

    def clean(self):
        cleaned_data = super().clean()
        item_type = cleaned_data.get('item_type')
        custom_item_type = cleaned_data.get('custom_item_type')

        # If 'other' is selected as the item type, ensure that the 'custom_item_type' is filled
        if item_type == 'other' and not custom_item_type:
            self.add_error('custom_item_type', 'Please specify the custom item type.')
        
        return cleaned_data
