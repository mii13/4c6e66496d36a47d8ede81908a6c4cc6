import logging
from django.utils import timezone
from django.db import models
from django.utils.safestring import mark_safe
from django.core.files.base import ContentFile
from requests import RequestException
from .validate import validate_function
from .api_client import get_graph, get_coordinates, GraphCreateException

logger = logging.getLogger(__name__)


class Graph(models.Model):
    func = models.CharField(max_length=100, verbose_name="function", validators=[validate_function, ],
                            help_text="allowed symbols: t, *, -, +, /, 0-9")
    interval = models.PositiveSmallIntegerField(verbose_name="depth",
                                                help_text="the depth of the simulation period in days")
    dt = models.PositiveSmallIntegerField(verbose_name="step", help_text="step in hours")
    graph = models.ImageField(upload_to='graphs', null=True)
    error = models.TextField(verbose_name="error", null=True, blank=True)
    handling_date = models.DateTimeField(null=True, verbose_name="handling date")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Graph'
        verbose_name_plural = 'Graphs'

    def __str__(self):
        return self.func

    def update_graph(self):
        self.graph.delete(save=False)
        self.create_graph()

    def create_graph(self):
        try:
            x_points, y_points = get_coordinates(self.func, self.interval, self.dt)
            graph_raw = get_graph(self.func, x_points, y_points)
            self.graph.save("{}_obj.png".format(self.id),
                            ContentFile(graph_raw),
                            save=False)
        except (GraphCreateException, RequestException, OSError) as e:
            logger.exception(e)
            self.error = str(e)
        self.handling_date = timezone.now()
        self.save()

    def graph_display(self):
        if not self.graph:
            return self.error
        return mark_safe('<img src="{}" />'.format(self.graph.url))

    graph_display.short_description = 'Graph'

    # def save(self, *args, **kwargs):
    #     pass
