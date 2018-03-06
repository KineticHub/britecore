from django.apps import apps
from rest_framework import serializers
from insurance.models import Risk, RiskType, RiskField, RiskFieldValue, TextField, NumberField, DateField, EnumField


class RiskFieldValueRelatedField(serializers.ModelSerializer):

    def to_internal_value(self, data):
        request = self.context['request']
        print request.data
        print request.method
        risk_type = RiskType.objects.get(name=request.data['type'])
        risk_field = RiskField.objects.get(name=data['name'], risk_type=risk_type)
        model_data = {'field': risk_field, data['field_type']: data.get('value', None)}
        FieldModel = apps.get_model('insurance', RiskField.FIELD_MODELS[data['field_type']])

        field_value = None

        if request.method == 'POST':
            model_data[data['field_type']] = FieldModel.convert_value(data.get('value', None))
            field_value = FieldModel.objects.create(**model_data)
        elif request.method == 'PUT':
            risk = Risk.objects.get(uuid=request.data['uuid'])

            for field in risk.values.all():
                if field.field_object.field.name == data['name']:
                    setattr(field.field_object, data['field_type'], FieldModel.convert_value(data.get('value', None)))
                    field.field_object.save()
                    return field.field_object
            field_value = FieldModel.objects.create(**model_data)
            risk.values.create(field_object=field_value)

        return field_value

    def to_representation(self, value):
        return {'name': value.field_object.field.name,
                'value': getattr(value.field_object, value.field_object.field.field_type),
                'field_type': value.field_object.field.field_type
                }

    class Meta:
        model = RiskFieldValue
        fields = '__all__'


class RiskFieldSerializer(serializers.ModelSerializer):
    # field_choices = serializers.SerializerMethodField()

    class Meta:
        model = RiskField
        fields = ('name', 'field_type', 'field_choices')

    # def get_field_choices(self, obj):
    #     return [x.strip().lower() for x in obj.field_choices.split(',')]


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
        field_names = []
        for field_data in fields_data:
            if RiskField.objects.filter(risk_type=risk_type, name=field_data['name']).exists():
                RiskField.objects.filter(risk_type=risk_type, name=field_data['name']).update(**field_data)
            else:
                RiskField.objects.create(risk_type=risk_type, **field_data)
            field_names.append(field_data['name'])

        delete_fields = []
        for field in risk_type.fields.all():
            if field.name not in field_names:
                delete_fields.append(field.id)
        risk_type.fields.filter(id__in=delete_fields).delete()
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
            RiskFieldValue.objects.create(risk=risk, field_object=field_object)
        return risk

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.save()
        return instance


# {
# 	"name": "Tim",
# 	"type": "automobile",
# 	"fields": [{
# 		"field_type": "text",
# 		"field_name": "model",
# 		"value": "little test"
# 	}]
# }