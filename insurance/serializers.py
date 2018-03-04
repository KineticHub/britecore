from django.apps import apps
from rest_framework import serializers
from insurance.models import Risk, RiskType, RiskField, RiskFieldValue, TextField, NumberField, DateField, EnumField


class RiskFieldValueRelatedField(serializers.ModelSerializer):

    def to_internal_value(self, data):
        request = self.context['request']
        risk_type = RiskType.objects.get(name=request.data['type'])
        risk_field = RiskField.objects.get(name=data['field_name'], risk_type=risk_type)
        model_data = {'field': risk_field, data['field_type']: data['value']}
        FieldModel = apps.get_model('insurance', RiskField.FIELD_MODELS[data['field_type']])
        field_value = FieldModel.objects.create(**model_data)
        return field_value

    def to_representation(self, value):
        return {'field_name': value.field_object.field.name,
                'value': value.field_object.text,
                'field_type': value.field_object.field.field_type
                }

    class Meta:
        model = RiskFieldValue
        fields = '__all__'


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
        for field_data in fields_data:
            RiskField.objects.create(risk_type=risk_type, **field_data)
        return risk_type


class RiskSerializer(serializers.ModelSerializer):
    type = serializers.StringRelatedField(source='risk_type')
    fields = RiskFieldValueRelatedField(many=True, source='values')

    class Meta:
        model = Risk
        fields = ('uuid', 'name', 'type', 'fields')

    def create(self, validated_data):
        request = self.context['request']
        field_value_objects = validated_data.pop('values')

        validated_data['risk_type'] = RiskType.objects.get(name=request.data['type'])
        risk = Risk.objects.create(**validated_data)

        for field_object in field_value_objects:
            print field_object
            RiskFieldValue.objects.create(risk=risk, field_object=field_object)
        return risk


# {
# 	"name": "Tim",
# 	"type": "automobile",
# 	"fields": [{
# 		"field_type": "text",
# 		"field_name": "model",
# 		"value": "little test"
# 	}]
# }