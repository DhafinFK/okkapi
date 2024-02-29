from rest_framework import serializers
from okk.models import Fakultas
from ..models import Mahasiswa
from okk.serializers import FakultasSerializer


class MahasiswaSerializer(serializers.ModelSerializer):
    fakultas_id = serializers.UUIDField(write_only=True, allow_null=True, required=False)
    fakultas = FakultasSerializer(read_only=True)

    class Meta:
        model = Mahasiswa
        fields = ['id', 'nama', 'npm', 'fakultas', 'angkatan', 'fakultas_id']
        read_only = [id,]
    
    def create(self, validated_data):
        fakultas_id = validated_data.pop('fakultas_id', None)
        if fakultas_id:
            validated_data['fakultas'] = Fakultas.objects.get(id=fakultas_id)
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        fakultas_id = validated_data.pop('fakultas_id', None)
        if fakultas_id:
            instance.fakultas = Fakultas.objects.get(id=fakultas_id)
            instance.save()
        return super().update(instance, validated_data)
