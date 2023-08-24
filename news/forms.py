from django import forms
from news.models import Categories

class CreateCategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({
            "maxlength": 200,
            "required": True
        })
        self.fields["name"].label = "Nome"
