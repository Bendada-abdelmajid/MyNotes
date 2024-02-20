from django import forms
from core.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('tag','description', 'remind_me_at')
    tag = forms.CharField( 
        widget=forms.TextInput(attrs={'placeholder': 'add tag',
                'class': 'block w-full bg-input px-3 py-2 rounded-md mb-5'}),
    )
    description = forms.CharField(
        required=False,  # Set to True if you want this field to be required
        widget=forms.Textarea(attrs={ 'class': 'block w-full bg-input  px-3 py-2 rounded-md h-[200px] resize-none mb-5'}),
    )
    remind_me_at = forms.DateTimeField(
        required=False,  # Set to True if you want this field to be required
        widget=forms.DateInput(attrs={ 'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'block w-full  bg-input  px-3 py-2 rounded-md '}),
    )