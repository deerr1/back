from rest_framework import serializers

from . import models


class InfoInstSerializer(serializers.ModelSerializer):
    """
    Сериализатор информации о институте
    """

    class Meta:
        model = models.InfoInstitutions
        fields = '__all__'
        depth = 2