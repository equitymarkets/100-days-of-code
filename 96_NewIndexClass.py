#Day 96: Successfully changed a method to a class and added new get and post methods to that class (URL: index.html homepage)



class Index_view(TemplateView):
    template_name = 'forest/index.html'
    
    def get(self, request):
        form = OfferForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = OfferForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)
