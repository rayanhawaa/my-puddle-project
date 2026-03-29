from django import forms

from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = {'content',}
        widgets = {
            'content': forms.Textarea(attrs={
                'style':'width:100%; padding:0.6rem 0.4rem; border-radius:10px; border:1px solid;'
            })
        }