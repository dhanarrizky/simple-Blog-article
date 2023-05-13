from django import forms
from .models import Post,category, comment

choices = category.objects.all().values_list('name','name')

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title','title_tag','category','author','body','image')
        
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control ', 'placeholder':'title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control ', 'placeholder':'title tag'}),
            #'image':forms.ImageField(attrs={'class':'form-control ', 'placeholder':'image'}),
            #'author':forms.Select(attrs={'class':'form-control ', 'placeholder':'author'}),
            'category':forms.Select(choices=choices,attrs={'class':'form-control ', 'placeholder':'category'}),
            'author':forms.TextInput(attrs={'class':'form-control', 'value' : '', 'id':'elder', 'type':'hidden'}),
            'body':forms.Textarea(attrs={'class':'form-control mb-3', 'placeholder':'Your Post'}),
        }
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('name','email','body')
        
        widgets = {
                'post':forms.TextInput(attrs={'class':'form-control', 'value' : '', 'id':'elder', 'type':'hidden'}),
                'name':forms.TextInput(attrs={'class':'form-control ', 'placeholder':'name'}),
                'email':forms.EmailInput(attrs={'class':'form-control ', 'placeholder':'email'}),
                'body':forms.Textarea(attrs={'class':'form-control mb-3', 'placeholder':'Comments..'}),
        }