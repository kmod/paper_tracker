import urllib

from django.shortcuts import render, get_object_or_404, redirect

from .models import Paper, Collection, CollectionPapers

def cpaper(request, collection_id, paper_id):
    memb = get_object_or_404(CollectionPapers, collection_id=collection_id, paper_id=paper_id)

    if request.method == "POST":
        memb.paper.title = request.POST['title']
        memb.paper.pdf_url = request.POST['pdf_url']
        memb.paper.year = int(request.POST['year'])
        memb.paper.publication = request.POST['publication']
        memb.notes = request.POST['notes']
        memb.priority = int(request.POST['priority'])
        memb.intro_conclusion_read = request.POST.get('intro_conclusion_read', False)
        memb.refs_expanded = request.POST.get('refs_expanded', False)
        memb.paper_read = request.POST.get('paper_read', False)
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
    cid = int(request.GET['cid'])

    if request.method == "POST":
        url = request.POST['url']
        p.pdf_url = url
        p.save()

        return redirect("/collection/%d/edit/%s?back=/collection/%d" % (cid, paper_id, cid))

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
        return (memb.paper_read and memb.refs_expanded, -memb.priority + (memb.refs_expanded or memb.paper_read),
                memb.intro_conclusion_read, memb.paper.title)
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
        try:
            p = Paper.objects.get(title=request.POST['Title'].strip())
        except Paper.DoesNotExist:
            p = Paper(title=request.POST['Title'].strip())
        p.year = int(request.POST['year'] or '0')
        p.publication = request.POST['publication'].strip()
        p.save()

        add_to = int(request.GET['add_to'])
        print(Collection.objects.get(pk=add_to).collectionpapers_set)
        p.collectionpapers_set.create(collection_id=int(request.GET['add_to']), priority=int(request.POST['Priority']))
        print(Collection.objects.get(pk=add_to).collectionpapers_set)
        p.save()
        print(Collection.objects.get(pk=add_to).collectionpapers_set)

        return redirect("/collection/%s" % request.GET['add_to'])

    context = {
    }
    return render(request, "papers/paper_new.html", context)
