from rest_framework import serializers
from insurance.models import Risk, RiskType, RiskField


class RiskFieldValueRelatedField(serializers.RelatedField):

    def to_representation(self, value):
        return {'name': value.field_object.field.name,
                'value': value.field_object.text,
                'type': value.field_object.field.field_type
                }


class RiskFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = RiskField
        fields = ('name', 'field_type', 'field_choices')


class RiskTypeSerializer(serializers.ModelSerializer):
    fields = RiskFieldSerializer(many=True)

    class Meta:
        model = RiskType
        fields = ('name', 'fields')

    def create(self, validated_data):
        print validated_data
        fields_data = validated_data.pop('fields')
        risk_type = RiskType.objects.create(**validated_data)
        for field_data in fields_data:
            RiskField.objects.create(risk_type=risk_type, **field_data)
        return risk_type

    def update(self, instance, validated_data):
        fields_data = validated_data.pop('fields')
        risk_type = RiskType.objects.get(name=validated_data['name'])
        risk_type.fields.all().delete()
        for field_data in fields_data:
            RiskField.objects.create(risk_type=risk_type, **field_data)
        return risk_type


class RiskSerializer(serializers.ModelSerializer):
    type = serializers.StringRelatedField(source='risk_type')
    fields = RiskFieldValueRelatedField(many=True, read_only=True, source='values')

    class Meta:
        model = Risk
        fields = ('uuid', 'name', 'type', 'fields')
