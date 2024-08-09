from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','body','status')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter UserName','value':'', 'id':'user1', 'type':'hidden'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','body','status')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            # 'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
        }

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }