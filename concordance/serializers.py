from rest_framework import serializers
from .models import Concordance, Corpus

class ConcordanceSerializer(serializers.ModelSerializer):
    class Meta:
        # Model that is being serialized
        model = Corpus
        fields = ('corpus_name')