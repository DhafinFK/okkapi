from rest_framework import serializers
from .models import Acara

class AcaraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acara
        fields = ['id', 'nama', 'waktu_mulai', 'waktu_selesai'] 
        read_only = (id,)

    def validate(self, data):
        """
        check start can't be later or equal to end datetime
        """

        waktu_mulai = data.get('waktu_mulai', getattr(self.instance, 'waktu_mulai', None))
        waktu_selesai = data.get('waktu_selesai', getattr(self.instance, 'waktu_selesai', None))


        if waktu_mulai >= waktu_selesai:
            raise serializers.ValidationError("Datetime mulai acara harus sebelum waktu selesai")
        
        return data