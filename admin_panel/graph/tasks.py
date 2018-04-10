import collections
from admin_panel.celery import app
from .models import Graph

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task
def update_graph_task(id_list):
    logger.info(id_list)
    if not isinstance(id_list, collections.Iterable):
        raise TypeError("{} not iterable".format(id_list))
    qs = Graph.objects.filter(id__in=id_list)
    for graph in qs:
        graph.update_graph()
