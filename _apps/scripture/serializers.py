from rest_framework import serializers
from _apps.scripture.models import Verse

class VerseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verse
