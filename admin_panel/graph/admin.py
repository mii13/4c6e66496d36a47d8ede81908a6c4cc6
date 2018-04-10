from django.contrib import admin
from django.contrib import messages
from .models import Graph
from .tasks import update_graph_task


@admin.register(Graph)
class GraphAdmin(admin.ModelAdmin):
    exclude = ("graph", "handling_date", "error")
    list_display = ('func', 'graph_display', 'interval', 'dt', 'handling_date')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.create_graph()

    def update_graph(self, request, queryset):
        id_list = list(queryset.values_list('id', flat=True))
        update_graph_task.delay(id_list)
        self.message_user(request,
                          "Successfully send task update graph",
                          messages.SUCCESS)

    actions = [update_graph, ]
    update_graph.short_description = "Update Graph"
