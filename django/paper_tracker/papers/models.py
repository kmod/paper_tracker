from django.db import models

# Create your models here.
class Paper(models.Model):
    title = models.CharField(max_length=255)
    pdf_url = models.TextField(default="", blank=True)

    def __str__(self):
        return "%s" % (self.title,)

class Collection(models.Model):
    name = models.CharField(max_length=255)
    papers = models.ManyToManyField(Paper, through='CollectionPapers')

    def __str__(self):
        # return "Collection %d: %s" % (self.pk, self.name)
        return "Collection %d: %s, with %d papers" % (self.pk, self.name, len(self.papers.all()))

class CollectionPapers(models.Model):
    paper = models.ForeignKey(Paper)
    collection = models.ForeignKey(Collection)

    priority = models.IntegerField(default=1)
    read = models.IntegerField(default=0)
    notes = models.TextField(default="", blank=True)
