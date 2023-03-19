from django.db import models


class Diagram(models.Model):
    diagram_name = models.CharField(max_length=15)
    fields = models.CharField(max_length=5000, default='')
    ready = models.BooleanField(default=False)

    def __str__(self):
        return self.diagram_name
