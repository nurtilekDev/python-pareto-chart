from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:diagram_id>/fill', views.diagram_fill, name="diagram_fill"),
    path('<int:diagram_id>/set', views.diagram_set, name="diagram_set"),
    path('<int:diagram_id>/view', views.diagram_view, name="diagram_view"),
]