from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from organisasi.models import BidangKepanitiaan
from ..models import Panitia, Mahasiswa


class PanitiaSerializer(serializers.ModelSerializer):
    mahasiswa = serializers.SerializerMethodField()
    bidang = serializers.SerializerMethodField()
    mahasiswa_id = serializers.UUIDField(write_only = True)
    bidang_id = serializers.UUIDField(write_only = True)

    class Meta:
        model = Panitia
        fields = ['id', 'mahasiswa', 'jabatan', 'bidang', 'mahasiswa_id', 'bidang_id']
        read_only = [id,]

    def get_mahasiswa(self, instance):
        mahasiswa = instance.mahasiswa
        return {
            "nama": mahasiswa.nama,
            "npm": mahasiswa.npm,
            "fakutlas": mahasiswa.fakultas.nama_panggilan
        }
    
    def get_bidang(self, instance):
        bidang = instance.bidang
        return bidang.nama


    
    def validate(self, data):
        jabatan = data.get('jabatan', getattr(self.instance, 'jabatan', None))
        bidang_id = data.get('bidang_id', getattr(self.instance, 'bidang_id', None))
        
        if (not bidang_id) or (not jabatan):
            raise ValidationError('json fields kurang')
        
        # Fetch the bidang_kepanitiaan instance to check its type
        try:
            bidang = BidangKepanitiaan.objects.get(id=bidang_id)
        except BidangKepanitiaan.DoesNotExist:
            raise ValidationError({"bidang_id": "Bidang Kepanitiaan not found."})

        # Define the valid combinations
        valid_combinations = {
            'BPH-PJ': 'BPH',
            'BPH-WAPJ': 'BPH',
            'STAFF': 'BPH',
            'PI': 'PI',
        }

        # Check if the combination is valid
        expected_bidang = valid_combinations.get(jabatan)
        if bidang.bidang_panitia != expected_bidang:
            raise ValidationError(f"The jabatan '{jabatan}' is not valid for the bidang '{bidang.bidang_panitia}'.")
        
        jabatan = data.get('jabatan')
        bidang_id = data.get('bidang_id')

        panitia_instance = Panitia.objects.filter(jabatan=jabatan, bidang__id=bidang_id).first()
        if panitia_instance and jabatan != "STAFF":
            if jabatan == "BPH-WAPJ":
                wapj = len(Panitia.objects.filter(jabatan=jabatan, bidang__id=bidang_id))
                if wapj >= 2:
                    raise ValidationError('WAPJ hanya bisa 2 per bidang')
            else:
                raise ValidationError('Jabatan sudah diambil oleh panitia lain')
                
        return data
    
    def create(self, validated_data):
        mahasiswa_id = validated_data.pop('mahasiswa_id')
        bidang_id = validated_data.pop('bidang_id')
        jabatan = validated_data.pop('jabatan')

        mahasiswa = Mahasiswa.objects.get(id=mahasiswa_id)
        bidang = BidangKepanitiaan.objects.get(id=bidang_id)

        panitia = Panitia.objects.create(mahasiswa=mahasiswa, bidang=bidang, jabatan=jabatan)
        return panitia
    
    def update(self, instance, validated_data):
        bidang = validated_data.get('bidang_id', None)
        jabatan = validated_data.get('jabatan', None)
        
        if bidang is not None:
            try:
                bidang = BidangKepanitiaan.objects.get(id=bidang)
                instance.bidang = bidang
            except BidangKepanitiaan.DoesNotExist:
                raise serializers.ValidationError('Bidang tidak exist')
        
        if jabatan is not None:
            instance.jabatan = jabatan
        
        instance.save()
        return instance