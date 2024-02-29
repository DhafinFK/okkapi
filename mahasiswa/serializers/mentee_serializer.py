from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from ..models import Mentee
from kelompok.models import Kelompok
from mahasiswa.models import Mahasiswa

class MenteeSerializer(serializers.ModelSerializer):
    mahasiswa = serializers.SerializerMethodField()
    kelompok = serializers.SerializerMethodField()
    nomor = serializers.IntegerField(write_only=True, allow_null=True, required=False)
    mahasiswa_id = serializers.UUIDField(write_only=True, allow_null=True, required=False)

    class Meta:
        model = Mentee
        fields = ['id', 'mahasiswa', 'kelompok', 'nomor', 'mahasiswa_id', 'jalur_masuk']
        read_only = [id,]

    def get_mahasiswa(self, instance):
        mahasiswa = instance.mahasiswa
        return {
            "nama": mahasiswa.nama,
            "npm": mahasiswa.npm,
            "fakutlas": mahasiswa.fakultas.nama_panggilan
        }

    def get_kelompok(self, instance):
        kelompok = instance.kelompok
        return {
            "id": kelompok.id,
            "nomor": kelompok.nomor
        }
    
    def validate_nomor(self, data):
        try:
            kel = Kelompok.objects.get(nomor=data)
        except Kelompok.DoesNotExist:
            raise ValidationError('Kelompok tidak exist')
        return data
    
    def validate_mahasiswa_id(self, data):
        if not Mahasiswa.objects.get(id=data):
            raise ValidationError('Mahasiswa tidak ditemukan')
        return data
    
    def create(self, validated_data):
        mahasiswa_id = validated_data.pop('mahasiswa_id')
        Kelompok_id = validated_data.pop('nomor')
        jalur_masuk = validated_data.pop('jalur_masuk')

        mahasiswa = Mahasiswa.objects.get(id=mahasiswa_id)
        kelompok = Kelompok.objects.get(nomor=Kelompok_id)

        mentee = Mentee.objects.create(
            mahasiswa=mahasiswa, 
            kelompok=kelompok, 
            jalur_masuk=jalur_masuk
        )

        return mentee
    
    def update(self, instance, validated_data):
        nomor = validated_data.get('nomor', None)
        
        if nomor is not None:
            try:
                kelompok = Kelompok.objects.get(nomor=nomor)
                instance.kelompok = kelompok
            except Kelompok.DoesNotExist:
                raise serializers.ValidationError('Kelompok tidak exist')
        
        instance.save()
        return instance