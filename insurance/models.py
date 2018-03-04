import uuid
from django.db import models
from django.apps import apps
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Risk(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    risk_type = models.ForeignKey('RiskType')

    def __str__(self):
        return self.name + ' ' + str(self.risk_type)


class RiskFieldValue(models.Model):

    risk = models.ForeignKey(Risk, related_name='values')

    # setup a generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    field_object = GenericForeignKey()

    def __str__(self):
        return str(self.field_object)


class RiskType(models.Model):
    name = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return str(self.name)


class RiskField(models.Model):
    TEXT = 'text'
    NUMBER = 'number'
    DATE = 'date'
    ENUM = 'enum'

    FIELD_TYPES = (
        (TEXT, 'text'),
        (NUMBER, 'number'),
        (DATE, 'date'),
        (ENUM, 'enum'),
    )

    FIELD_MODELS = {
        TEXT: 'TextField',
        NUMBER: 'NumberField',
        DATE: 'DateField',
        ENUM: 'EnumField'
    }

    name = models.CharField(max_length=255)
    risk_type = models.ForeignKey(RiskType, related_name="fields", on_delete=models.CASCADE)
    field_type = models.CharField(max_length=6, choices=FIELD_TYPES)
    field_choices = models.TextField(default="", blank=True,
                                     help_text="If you are allowing the user to choose from preselected options via "
                                               "the enum type, please list the options here separated by a comma.")

    class Meta:
        unique_together = ("risk_type", "name")

    def __str__(self):
        return str(self.risk_type) + " " + self.name


class BaseField(models.Model):
    field = models.ForeignKey(RiskField)
    risk = GenericRelation(RiskFieldValue)

    class Meta:
        abstract = True


class TextField(BaseField):
    text = models.TextField()

    def __str__(self):
        return str(self.text)


class NumberField(BaseField):
    number = models.IntegerField()

    def __str__(self):
        return str(self.number)


class DateField(BaseField):
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class EnumField(BaseField):
    choice = models.TextField()

    def __str__(self):
        return str(self.choice)
