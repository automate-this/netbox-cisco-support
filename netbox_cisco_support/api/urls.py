from netbox.api.routers import NetBoxRouter
from netbox_cisco_support import views

router = NetBoxRouter()
router.register('cisco-device-type-support', views.CiscoDeviceTypeSupportViewSet)
router.register('cisco-support', views.CiscoSupportViewSet)

urlpatterns = router.urls
