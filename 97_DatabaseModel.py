#Day 97
#from models.py:

class Post(models.Model):
    post = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

#New forms.py:
 
from django import forms
from forest.models import Post

class OfferForm(forms.ModelForm):
    post = forms.CharField()
    
    class Meta:
        model = Post
        fields = ('post',)

class TradeForm(forms.Form):
    post = forms.CharField()


#New index view in views.py:

class Index_view(TemplateView):
    template_name = 'forest/index.html'
    
    def get(self, request):
        form = OfferForm()
        posts = Post.objects.all()
        args = {'form': form, 'posts': posts}
        return render(request, self.template_name, args)
    
    def post(self, request):
        form = OfferForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['post']
            form = OfferForm()
        args = {'form': form, 'text': text}
        
        return render(request, self.template_name, args)
 

