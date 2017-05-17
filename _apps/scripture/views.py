from rest_framework import viewsets
from _apps.scripture.models import Verse
from _apps.scripture.serializers import VerseSerializer


class VerseViewSet(viewsets.ModelViewSet):
    queryset = Verse.objects.all()
    serializer_class = VerseSerializer
