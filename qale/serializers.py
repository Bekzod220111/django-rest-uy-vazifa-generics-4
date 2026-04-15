from rest_framework.serializers import ModelSerializer
from .models import Qale

class QaleSerializer(ModelSerializer):
    
    class Meta:
        model = Qale
        fields = '__all__'