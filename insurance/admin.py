from django.contrib import admin
from insurance.models import Risk, RiskFieldValue, RiskType, RiskField, TextField


admin.site.register(RiskType)
admin.site.register(RiskField)

admin.site.register(Risk)
admin.site.register(TextField)
admin.site.register(RiskFieldValue)