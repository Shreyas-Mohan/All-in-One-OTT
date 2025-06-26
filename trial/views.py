from django.shortcuts import render
from .models import content, Store
from django.shortcuts import get_object_or_404
from .forms import contentForm

def all_trial(request):
   trials = content.objects.all()
   return render(request, 'all_trial.html', {'trials': trials})

def trial_detail(request, trial_id):
   trial = get_object_or_404(content, pk=trial_id)
   return render(request, 'trial_detail.html', {'trial':trial})

def trial_store_view(request):
   stores = None 
   if(request.method == 'POST'):
      form = contentForm(request.POST)
      if form.is_valid():
         content = form.cleaned_data['content']
         stores = Store.objects.filter(contents=content)
   else:
      form = contentForm() 
   return render(request, 'trial_stores.html', {'stores':stores, 'form':form})
