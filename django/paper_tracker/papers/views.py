from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Paper, Collection

def papers_index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def collections_index(request):
    collections = Collection.objects.all()
    context = {
        'collections': collections,
    }
    return render(request, "papers/collections.html", context)

def collection(request, collection_id):
    c = get_object_or_404(Collection, pk=collection_id)
    context = {
        'collection': c,
    }
    return render(request, "papers/collection.html", context)
