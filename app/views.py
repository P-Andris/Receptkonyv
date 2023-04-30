from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q

from .models import *
from .forms import ReceptForm
from .filters import ReceptFilter

receptId = None

def index(request):
    global receptId

    receptek = Recept.objects.all()

    receptFilter = ReceptFilter(request.GET, queryset = receptek)

    recept = receptek.filter(Q(id__exact = receptId)).first()

    context = {
        'receptek': receptek,
        'receptFilter': receptFilter,
        'recept': recept
    }

    return render(request, 'index.html', context = context)

def ujRecept(request):
    form = ReceptForm(request.POST or None)
    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect(index)
    else:
        form = ReceptForm()

    context = {
        'form': form
    }

    return render(request, 'uj_recept.html', context = context)

def receptTorlese(request, id):
    recept = get_object_or_404(Recept, pk = id)
    recept.delete()
    return redirect(index)

# Főoldal frissítése:
def indexFrissites(request, id):
    global receptId
    receptId = id
    return redirect(index)