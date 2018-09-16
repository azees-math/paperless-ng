from django_filters.rest_framework import CharFilter, FilterSet, BooleanFilter

from .models import Correspondent, Document, Tag, DocumentType


class CorrespondentFilterSet(FilterSet):

    class Meta:
        model = Correspondent
        fields = {
            "name": [
                "startswith", "endswith", "contains",
                "istartswith", "iendswith", "icontains"
            ],
            "slug": ["istartswith", "iendswith", "icontains"]
        }


class TagFilterSet(FilterSet):

    class Meta:
        model = Tag
        fields = {
            "name": [
                "startswith", "endswith", "contains",
                "istartswith", "iendswith", "icontains"
            ],
            "slug": ["istartswith", "iendswith", "icontains"]
        }


class DocumentTypeFilterSet(FilterSet):

    class Meta(object):
        model = DocumentType
        fields = {
            "name": [
                "startswith", "endswith", "contains",
                "istartswith", "iendswith", "icontains"
            ],
            "slug": ["istartswith", "iendswith", "icontains"]
        }


class DocumentFilterSet(FilterSet):

    CHAR_KWARGS = {
        "lookup_expr": (
            "startswith",
            "endswith",
            "contains",
            "istartswith",
            "iendswith",
            "icontains"
        )
    }

    correspondent__name = CharFilter(
        field_name="correspondent__name", **CHAR_KWARGS)
    correspondent__slug = CharFilter(
        field_name="correspondent__slug", **CHAR_KWARGS)
    tags__name = CharFilter(
        field_name="tags__name", **CHAR_KWARGS)
    tags__slug = CharFilter(
        field_name="tags__slug", **CHAR_KWARGS)
    tags__empty = BooleanFilter(
        field_name="tags", lookup_expr="isnull", distinct=True)
    document_type__name = CharFilter(
        field_name="document_type__name", **CHAR_KWARGS)
    document_type__slug = CharFilter(
        field_name="document_type__slug", **CHAR_KWARGS)

    class Meta:
        model = Document
        fields = {
            "title": [
                "startswith", "endswith", "contains",
                "istartswith", "iendswith", "icontains"
            ],
            "content": ["contains", "icontains"],
        }
