from rest_framework import serializers
from models import Instrument


class InstrumentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instrument
        fields = '__all__'