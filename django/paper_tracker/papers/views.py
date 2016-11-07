import urllib

from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse

from .models import Paper, Collection, CollectionPapers

def cpaper(request, collection_id, paper_id):
    memb = get_object_or_404(CollectionPapers, collection_id=collection_id, paper_id=paper_id)

    if request.method == "POST":
        memb.paper.title = request.POST['title']
        memb.paper.pdf_url = request.POST['pdf_url']
        memb.notes = request.POST['notes']
        memb.priority = int(request.POST['priority'])
        memb.save()
        memb.paper.save()
        return redirect(urllib.parse.unquote(request.GET['back']))

    context = {
        'memb': memb,
        'back_url': request.GET['back'],
    }
    return render(request, "papers/cpaper.html", context)


def papers_index(request):
    papers = Paper.objects.all()
    context = {
        'papers': papers,
    }
    return render(request, "papers/papers.html", context)

def paper_delete(request, paper_id):
    p = get_object_or_404(Paper, pk=paper_id)
    if request.method == "POST":
        p.delete()
        return redirect(urllib.parse.unquote(request.GET['back']))

    p = get_object_or_404(Paper, pk=paper_id)
    context = {
        'back_url': request.GET['back'],
    }
    return render(request, "papers/paper_delete.html", context)


def paper_findpdf(request, paper_id):
    p = get_object_or_404(Paper, pk=paper_id)
    if request.method == "POST":
        url = request.POST['url']
        p.pdf_url = url
        p.save()
        return redirect(urllib.parse.unquote(request.GET['back']))

    context = {
        'paper': p,
        'search_query': urllib.parse.quote(p.title),
    }
    return render(request, "papers/paper_findpdf.html", context)

def collections_index(request):
    collections = Collection.objects.all()
    context = {
        'collections': collections,
    }
    return render(request, "papers/collections.html", context)

def collection(request, collection_id):
    c = get_object_or_404(Collection, pk=collection_id)
    def key(memb):
        return (-memb.read / 30, -memb.priority, memb.paper.title)
    membs = sorted(c.collectionpapers_set.all(), key=key)

    context = {
        'collection': c,
        'back_url': urllib.parse.quote(request.get_full_path()),
        'members': membs
    }
    return render(request, "papers/collection.html", context)

def paper_new(request):
    if request.method == "POST":
        assert request.POST["Title"]
        p = Paper(title=request.POST['Title'])
        p.priority = int(request.POST['Priority'])
        p.save()

        add_to = int(request.GET['add_to'])
        print(Collection.objects.get(pk=add_to).collectionpapers_set)
        p.collectionpapers_set.create(collection_id=int(request.GET['add_to']))
        print(Collection.objects.get(pk=add_to).collectionpapers_set)
        p.save()
        print(Collection.objects.get(pk=add_to).collectionpapers_set)

        return redirect("/collection/%s" % request.GET['add_to'])

    context = {
    }
    return render(request, "papers/paper_new.html", context)

