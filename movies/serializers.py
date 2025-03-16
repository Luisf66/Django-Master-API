from movies.models import Movie
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self,value):
        if value.year < 1990:
            raise serializers.ValidationError('A data não deve ser menor que 1990')
        return value
    