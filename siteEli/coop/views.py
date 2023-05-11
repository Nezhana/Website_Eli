from django.shortcuts import render, redirect
from .forms import CooperationForm, CollaboratorForm
from .models import Cooperation, Collaborator
from django.core.exceptions import ValidationError

# Create your views here.

def index(request):


    if request.method == 'POST':
        form_child = CooperationForm(request.POST)
        form_2 = CollaboratorForm(request.POST)
        email = request.POST['email']

        if form_2.is_valid():
            form_2 = form_2.save()
            if form_child.is_valid():
                form = form_child.save(commit=False)
                form.email = form_2
                form.save()
        else:
            collabor = Collaborator.objects.get(email=email)
            form = form_child.save(commit=False)
            form.email = collabor
            form.save()

        return redirect('coop_done')

    form = CooperationForm()
    form_2 = CollaboratorForm()

    data = {
        'form': form,
        'form_2': form_2
    }

    return render(request, 'coop/coop.html', data)

def coop_done(request):

    return render(request, 'coop/coop-done.html')