import beam
from .models import Person, Organization, Note


class PersonNoteDetailInline(beam.RelatedInline):
    title = "Notes"
    fields = ["organization", "text", "modified_at", "created_at"]
    foreign_key_field = "person"
    model = Note


class PersonViewSet(beam.ViewSet):
    model = Person
    fields = ["first_name", "last_name"]

    detail_fields = fields + ["employers"]
    detail_inline_classes = [PersonNoteDetailInline]


class NoteInline(beam.RelatedInline):
    title = "Notes"
    foreign_key_field = "organization"
    model = Note
    fields = ["person", "text"]


class NoteDetailInline(NoteInline):
    fields = ["person", "text", "modified_at", "created_at"]


class OrganizationViewSet(beam.ViewSet):
    model = Organization

    list_fields = ["name"]
    detail_fields = ["name", "employees", "modified_at", "created_at"]
    fields = ["name", "employees"]

    inline_classes = [NoteInline]
    detail_inline_classes = [NoteDetailInline]
