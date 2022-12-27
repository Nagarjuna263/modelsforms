from django import forms
from app1.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields="__all__"
        
class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        #fields="__all__"
        fields=['topic_name','name']
        #exclude=['name']
        help_texts={'topic_name':'shouldnot integers','name': 'only integers'}
        labels={'topic_name':'TN','name':'N'}
        widgets={'url':forms.PasswordInput,'name':forms.Textarea}
        
class AccessRecordsForm(forms.ModelForm):
    class Meta:
        model=AccessRecords
        fields="__all__"
        #fields=['date']
        #exclude=['name']