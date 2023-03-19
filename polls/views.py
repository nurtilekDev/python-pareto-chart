from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Diagram


# Create your views here.
def index(request):
    diagrams = get_list_or_404(Diagram)
    return render(request, 'polls/index.html', {'diagrams': diagrams})


def diagram_fill(request, diagram_id):
    diagram = get_object_or_404(Diagram, pk=diagram_id)
    return render(request, 'polls/diagram_fill.html', {'diagram': diagram})


def diagram_view(request, diagram_id):
    diagram = get_object_or_404(Diagram, pk=diagram_id)
    items = diagram.fields.split(',')

    def mapper(w):
        return w.split('=')

    data = list(map(mapper, items))
    return render(request, 'polls/diagram_view.html', {'diagram': diagram, 'items': data})


def diagram_set(request, diagram_id):
    diagram = get_object_or_404(Diagram, pk=diagram_id)
    try:
        key = request.POST['values']
    except (KeyError, Diagram.DoesNotExist):
        return render(request, 'polls/error.html')
    else:
        diagram.fields = key
        diagram.save()
        return redirect('polls:diagram_view', diagram_id=diagram_id)
