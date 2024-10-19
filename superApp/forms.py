from django import forms

class InputForm(forms.Form):
    Event=forms.CharField(label='Enter Event : ',max_length=50)
    Desc=forms.CharField(widget=forms.Textarea)
    