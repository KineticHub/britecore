from django.contrib import admin
from insurance.models import Risk, RiskFieldValue, RiskType, RiskField, TextField, NumberField, DateField, EnumField


class RiskAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'name', 'risk_type')
    list_select_related = ('risk_type',)
    search_fields = ['uuid', 'name']
    list_filter = ['risk_type__name']
    list_editable = ('name',)
    ordering = ('name',)
    readonly_fields = ('uuid',)


admin.site.register(Risk, RiskAdmin)

admin.site.register(RiskFieldValue)
admin.site.register(RiskType)
admin.site.register(RiskField)

admin.site.register(TextField)
admin.site.register(NumberField)
admin.site.register(DateField)
admin.site.register(EnumField)