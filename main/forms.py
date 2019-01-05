from django import forms

class AllForm(forms.Form):
    name = forms.CharField(label="Name ", max_length=20, empty_value='None')
    surname = forms.CharField(label="SubName ", max_length=20, empty_value='None', )
    fathername = forms.CharField(label="FatherName  ", max_length=20, empty_value='None', )
    phone = forms.CharField(label="Phone ",max_length=15,
                            widget=forms.TextInput(attrs={'pattern': '8-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}'}))
    description = forms.CharField(label="Description ",max_length=200,widget=forms.Textarea(attrs={'cols': '35', 'rows': '10'}),strip='')
    find = forms.CharField(label="Find ", max_length=20, empty_value='None')
    login = forms.CharField(label="Login ", max_length=20, empty_value='None')
    password = forms.CharField(label="Password ", max_length=20, empty_value='None',widget=forms.PasswordInput())
#attrs={'pattern': '2-[0-9]{3}-[0-9]{3}'}
#     phone = forms.RegexField(regex=r'[0-9]+',)
#type'="tel" pattern='2-[0-9]{3}-[0-9]{3}'
