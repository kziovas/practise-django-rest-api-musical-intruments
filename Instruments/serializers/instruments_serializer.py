from rest_framework import serializers
from Instruments.models import Instrument


class InstrumentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instrument
        fields = '__all__'