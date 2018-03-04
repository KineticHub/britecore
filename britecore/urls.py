from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework import routers
from insurance.views import RiskViewSet, RiskTypeViewSet


router = routers.DefaultRouter()
router.register(r'risks/types', RiskTypeViewSet, base_name='risks-types-view')
router.register(r'risks', RiskViewSet, base_name='risks-view')


urlpatterns = [
    url(r'^risks/$', TemplateView.as_view(template_name="insurance/risks/risks.html")),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
