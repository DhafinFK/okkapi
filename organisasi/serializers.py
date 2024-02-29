from rest_framework import serializers
from .models import BidangKepanitiaan, Rapat
from mahasiswa.models import Panitia


class BidangKepanitiaanSerializer(serializers.ModelSerializer):
    anggota = serializers.SerializerMethodField()

    class Meta:
        model = BidangKepanitiaan
        fields = ['id', 'nama', 'bidang_panitia', 'anggota']
        read_only = ['id',]

    def get_anggota(self, instance):
        anggotas = Panitia.objects.filter(bidang=instance).order_by('jabatan')
        lst = []
        for anggota in anggotas:
            mahasiswa = anggota.mahasiswa
            lst.append(
                {
                    "nama": mahasiswa.nama,
                    "jabatan": anggota.jabatan,
                    "id_panitia": anggota.id
                }
            ) 
        return lst

class RapatSerializer(serializers.ModelSerializer):
    attendees = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Panitia.objects.all(),
        required=False,
        allow_empty=True
    )

    class Meta:
        model = Rapat
        fields = ['id', 'bidang', 'date', 'start_time', 'end_time', 'attendees']

    def create(self, validated_data):
        attendees_data = validated_data.pop('attendees', [])
        mentoring_session = Rapat.objects.create(**validated_data)
        mentoring_session.attendees.set(attendees_data)
        return mentoring_session
    
    def update(self, instance, validated_data):
        attendees_data = validated_data.pop('attendees', None)
        for attributes, value in validated_data.items():
            setattr(instance, attributes, value)
        instance.save()
        if attendees_data is not None:
            instance.attendees.set(attendees_data)
        return instance