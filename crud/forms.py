from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    ImgName = forms.CharField(widget=forms.TextInput(attrs={'id': 'imgName', 'placeholder': 'Enter Image Name'}), 
                                            required=True, max_length=50, min_length=6)

    ImgURL = forms.CharField(widget=forms.TextInput(attrs={'id': 'imgURL', 'placeholder': 'Enter Image URL'}
                                                  ), required=True, max_length=10000)
                                                  
    ImgDetails = forms.CharField(widget=forms.Textarea(attrs={'id': 'imgDetails', 'placeholder': 'Enter Image Details'}
                                                     ), required=True, max_length=1000)
                                    
    class Meta:
        model = Image
        fields = ('ImgName', 'ImgURL', 'ImgDetails')


class ImageUpdateForm(forms.ModelForm):
    ImgURL = forms.CharField(widget=forms.TextInput(attrs={'id': 'imgURL', 'placeholder': 'Enter Image URL'}
                                                  ), required=True, max_length=10000)
                                                  
    ImgDetails = forms.CharField(widget=forms.Textarea(attrs={'id': 'imgDetails', 'placeholder': 'Enter Image Details'}
                                                     ), required=True, max_length=1000)
                                    
    class Meta:
        model = Image
        fields = ('ImgURL', 'ImgDetails')