from django

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'content', 'image')