from django.urls import path

from . import views

app_name = 'charts'
urlpatterns = [
    path('', views.charts, name='charts'),
    path('<int:diagram_id>/configure', views.configure, name="configure"),
    path('<int:diagram_id>/setup', views.setup, name="setup"),
    path('<int:diagram_id>/pareto', views.pareto_chart, name="pareto_chart"),
]