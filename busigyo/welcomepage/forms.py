from django import forms

class TestForm(forms.Form):
    num = forms.IntegerField(label='天気コード')


class Form(forms.Form):
	loc = forms.CharField(label = '', max_length='100', required=True)
	#lat = forms.FloatField(label='緯度')
	#lon = forms.FloatField(label='経度')
