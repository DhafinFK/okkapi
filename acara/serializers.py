from rest_framework import serializers
from .models import *


class AcaraSerializer(serializers.ModelSerializer):
    paket_sponsorship = serializers.PrimaryKeyRelatedField(
        many=True, 
        read_only=True, 
        source='sponsorship'
    )

    class Meta:
        model = Acara
        fields = ['id', 'nama', 'waktu_mulai', 'waktu_selesai', 'pembicara_list', 'paket_sponsorship'] 
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
    
    def create(self, validated_data):
        pembicara_list = validated_data.pop('pembicara_list', [])
        acara = Acara.objects.create(**validated_data)
        acara.pembicara_list.set(pembicara_list)
        return acara

    def update(self, instance, validated_data):
        pembicara_list = validated_data.pop('pembicara_list', None)
        if pembicara_list is not None:
            instance.pembicara_list.set(pembicara_list)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    

class PembicaraSerializer(serializers.ModelSerializer):
    mengisi_acara = serializers.PrimaryKeyRelatedField(
        many=True,
        source='mengisi',
        read_only=True,
        required=False
    )

    class Meta:
        model = Pembicara
        fields = ['id', 'nama', 'mengisi_acara']
        read_only  = [id,]
    

class SponsorSerializer(serializers.ModelSerializer):
    paket_sponsorship = serializers.PrimaryKeyRelatedField(
        many=True, 
        read_only=True, 
        source='sponsorship'
    )

    class Meta:
        model = Sponsor
        fields = ['id', 'nama', 'paket_sponsorship']
