from django.db import models

# Create your models here.
class Paper(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return "Paper %d: %s" % (self.pk, self.title)

class Collection(models.Model):
    name = models.CharField(max_length=255)
    papers = models.ManyToManyField(Paper)

    def __str__(self):
        # return "Collection %d: %s" % (self.pk, self.name)
        return "Collection %d: %s, with %d papers" % (self.pk, self.name, len(self.papers.all()))

