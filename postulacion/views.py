from django.shortcuts import render
from .forms import PostulantesForm
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.contrib import messages
from .models import postulantes


def postulacion(request):
    # messages.info(request, 'Hello World')
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostulantesForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostulantesForm()

    p = postulantes.objects.all()
    print(p)
    context = {'form': form,
               'data': p}

    return render(request, 'postulacion/postulacion.html', context)


def delete_postulante(request, my_id):
    try:
        obj = postulantes.objects.get(id=my_id)
        obj.delete()
    except postulantes.DoesNotExist:
        raise Http404

    return render(request, 'postulacion/deleted.html')
