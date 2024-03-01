from rest_framework import serializers
from .models import CustomUser
from mahasiswa.models import Mahasiswa

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    npm = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'npm')
        
    def create(self, validated_data):
        npm = validated_data.pop('npm', None)

        user = CustomUser(
            username=validated_data['username'], 
            email=validated_data['email']    
        )
        user.set_password(validated_data['password'])
        user.save()

        if npm:
            try:
                mahasiswa = Mahasiswa.objects.get(npm=npm)
                user.mahasiswa = mahasiswa
                user.save()
            except Mahasiswa.DoesNotExist:
                raise serializers.ValidationError({'npm': 'Npm tidak valid'})
            
        return user