from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']# which field to include from model
        labels = {'text': ''} #tells django not to generate a label for text field

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widget = { 'text': forms.Textarea(attrs={'cols': 80})} #making text field 80 columns wide
