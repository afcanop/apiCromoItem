from rest_framework import serializers
from inv.models.item import item


class itemSerializers(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = '__all__'
