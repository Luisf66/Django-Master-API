from movies.models import Movie
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        return 5

    def validate_release_date(self,value):
        if value.year < 1990:
            raise serializers.ValidationError('A data não deve ser menor que 1990')
        return value
    
    def validate_duration(self,value):
        if value < 0:
            raise serializers.ValidationError('A duração nao pode ser negativa')
        return value