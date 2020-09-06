from django import forms

class RequestForm(forms.Form):
    text = forms.CharField(
        widget=forms.TextInput
        (
            attrs={'value': '请输入手机品牌','onfocus':'javascript:if(this.value==\'请输入手机品牌\')this.value=\'\';'}
        )
    )
    start_time = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_time = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))