from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Diagram


# Create your views here.
def charts(request):
    diagrams = get_list_or_404(Diagram)
    return render(request, 'charts/index.html', {'diagrams': diagrams})


def configure(request, diagram_id):
    diagram = get_object_or_404(Diagram, pk=diagram_id)
    return render(request, 'charts/configure.html', {'diagram': diagram})


def pareto_chart(request, diagram_id):
    diagram = get_object_or_404(Diagram, pk=diagram_id)
    items = diagram.fields.split('\r\n')

    def mapper(w):
        return w.split('=')

    data = list(map(mapper, items))
    return render(request, 'charts/pareto.html', {'diagram': diagram, 'items': data})


def setup(request, diagram_id):
    diagram = get_object_or_404(Diagram, pk=diagram_id)
    try:
        key = request.POST['values']
    except (KeyError, Diagram.DoesNotExist):
        return render(request, 'polls/configure.html', {
            'error-message': 'Что-то пошло не так'
        })
    else:
        diagram.fields = key
        diagram.save()
        return redirect('charts:pareto_chart', diagram_id=diagram_id)
