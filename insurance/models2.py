from django.db import models


class RiskType(models.Model):
    name = models.CharField(unique=True, max_length=255)


class RiskField(models.Model):
    risk = models.ForeignKey(RiskType, related_name='%(class)ss'.lower(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ("risk", "name")
        abstract = True

    def __str__(self):
        return str(self.risk) + " " + self.name


class TextField(RiskField):
    text = models.TextField()


class NumberField(RiskField):
    number = models.IntegerField()


class DateField(RiskField):
    date = models.DateField()


class EnumField(RiskField):
    pass


class EnumOption(models.Model):
    enum = models.ForeignKey(EnumField, related_name='options', on_delete=models.CASCADE)
    option = models.CharField(max_length=255)

    class Meta:
        unique_together = ("enum", "option")

    def __str__(self):
        return str(self.enum) + " " + self.option
