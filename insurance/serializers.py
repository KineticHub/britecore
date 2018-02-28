from rest_framework import serializers
from insurance.models import Risk, RiskType, RiskField, RiskFieldValue, TextField


class FieldObjectRelatedField(serializers.RelatedField):

    def to_representation(self, value):
        return {'name': value.field_object.name, 'value':value.field_object.text, 'type':value.field_object.type}


class RiskFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = RiskField
        fields = ('name', 'field_type', 'field_choices')


class RiskTypeSerializer(serializers.ModelSerializer):
    fields = RiskFieldSerializer(many=True)

    class Meta:
        model = RiskType
        fields = ('name', 'fields')


class RiskSerializer(serializers.ModelSerializer):
    risk_type = serializers.StringRelatedField()
    fields = FieldObjectRelatedField(many=True, read_only=True, source='values')

    class Meta:
        model = Risk
        fields = ('uuid', 'name', 'risk_type', 'fields')
