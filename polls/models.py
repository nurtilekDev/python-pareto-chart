from django.db import models


class Diagram(models.Model):
    diagram_name = models.CharField(max_length=15)
    fields = models.CharField(max_length=5000)

    def __str__(self):
        return self.diagram_name


class Choice(models.Model):
    chosen_diagram = Diagram.diagram_name

    def __str__(self):
        return self.chosen_diagram
