from django import forms

from tiger.content.models import Content, PdfMenu, ItemImage


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        exclude = ['site']


class PdfMenuForm(forms.ModelForm):
    class Meta:
        model = PdfMenu
        exclude = ['site', 'page_count', 'featured']

    def __init__(self, data=None, site=None, *args, **kwargs):
        super(PdfMenuForm, self).__init__(data=data, *args, **kwargs)
        self.site = site
        self.fields['sections'].queryset = site.section_set.all()


class AddImageForm(forms.ModelForm):
    class Meta:
        model = ItemImage
        exclude = ['site']


class EditImageForm(forms.ModelForm):
    class Meta:
        model = ItemImage
        fields = ['title', 'description']
