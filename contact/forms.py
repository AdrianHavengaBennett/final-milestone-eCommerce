from django import forms


class ContactForm(forms.Form):
	name = forms.CharField(max_length=100,
		widget= forms.TextInput(
			attrs={'placeholder':'What is your name?'}),
		label=''
	)
	email = forms.EmailField(
		widget= forms.EmailInput(
			attrs={'placeholder':'What is your email address?'}),
		label=''
	)
	message = forms.CharField(
		widget=forms.Textarea(
			attrs={'placeholder':'How can we help?'}),
		label=''
	)
