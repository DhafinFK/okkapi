from rest_framework import serializers
from .models import Kelompok, MentoringSession
from mahasiswa.models import Mentee, Mentor
from mahasiswa.serializers import MenteeSerializer

class KelompokSerializer(serializers.ModelSerializer):
    mentor = serializers.SerializerMethodField()

    class Meta:
        model = Kelompok
        fields = ['id', 'nomor', 'mentor']
        read_only = [id,]

    def get_mentor(self, instance):
        mentor = Mentor.objects.filter(kelompok=instance).first()
        if mentor:
            mahasiswa = mentor.mahasiswa
            return {
                "nama": mahasiswa.nama, 
                "id_mahasiswa": mahasiswa.id, 
                "id_mentor": mentor.id}
        return None
    

class MentoringSerializer(serializers.ModelSerializer):
    attendees = serializers.PrimaryKeyRelatedField(
        many=True,         
        queryset=Mentee.objects.all(),
        required=False,  
        allow_empty=True  
    )

    class Meta:
        model = MentoringSession
        fields = ['id', 'kelompok', 'date', 'start_time', 'end_time', 'attendees']

    def check_attendees(self, attrs):
        attendees = attrs.get('attendees', None)
        kelompok = attrs.get('kelompok', getattr(self.instance, 'kelompok', None))

        if attendees:
            mentees = kelompok.mentee_set.all()
            for mentee_id in attendees:
                if mentee_id not in mentees:
                    raise serializers.ValidationError('mentee yang dimasukkan harus dari kelompok')
                
        return attrs

    def validate(self, attrs):
        attrs = self.check_attendees(attrs)

        start_time = attrs.get('start_time', getattr(self.instance, 'start_time', None))
        end_time = attrs.get('end_time', getattr(self.instance, 'end_time', None))

        if start_time >= end_time:
            raise serializers.ValidationError("Start time harus sebelum waktu selesai")
        
        return attrs

    def create(self, validated_data):
        attendees_data = validated_data.pop('attendees', [])
        mentoring_session = MentoringSession.objects.create(**validated_data)
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
