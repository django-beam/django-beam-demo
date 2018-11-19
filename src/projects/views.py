import beam
from projects.models import Project


class ProjectViewSet(beam.ViewSet):
    model = Project

    fields = ["name"]

