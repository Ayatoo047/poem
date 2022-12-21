from django.forms import ModelForm
from .models import Poems


class PoemForm(ModelForm):
    class Meta:
        model = Poems
        fields = ['title', 'description', 'featured_image']

    def __init__(self, *args, **kwargs):
        super(PoemForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})