from django import forms

class TestForm(forms.Form):
    num = forms.IntegerField(label='天気コード')