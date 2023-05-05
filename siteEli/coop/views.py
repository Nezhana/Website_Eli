from django.shortcuts import render, redirect
from .forms import CooperationForm

# Create your views here.

def index(request):

    if request.method == 'POST':
        form = CooperationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coop_done')
        else:
            pass

    form = CooperationForm()

    data = {
        'form': form
    }

    return render(request, 'coop/coop.html', data)

def coop_done(request):

    return render(request, 'coop/coop-done.html')