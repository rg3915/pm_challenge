from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Comment, Tag
from .serializers import (
    CommentCreateSerializer,
    CommentSerializer,
    TagSerializer
)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('text', 'tags__name')

    def get_serializer_class(self):
        if self.action == 'create':
            return CommentCreateSerializer
        return CommentSerializer
