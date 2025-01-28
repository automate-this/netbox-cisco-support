from netbox.api.viewsets import NetBoxModelViewSet
from netbox_cisco_support.models import CiscoDeviceTypeSupport, CiscoSupport
from netbox_cisco_support.serializers import CiscoDeviceTypeSupportSerializer, CiscoSupportSerializer

class CiscoDeviceTypeSupportViewSet(NetBoxModelViewSet):
    queryset = CiscoDeviceTypeSupport.objects.all()
    serializer_class = CiscoDeviceTypeSupportSerializer
    filterset_fields = [
        'device_type',
        'end_of_sale_date',
        'end_of_sw_maintenance_releases',
        'end_of_security_vul_support_date',
        'end_of_routine_failure_analysis_date',
        'end_of_service_contract_renewal',
        'last_date_of_support',
        'end_of_svc_attach_date',
    ]

class CiscoSupportViewSet(NetBoxModelViewSet):
    queryset = CiscoSupport.objects.all()
    serializer_class = CiscoSupportSerializer
    filterset_fields = [
        'device',
        'coverage_end_date',
        'warranty_end_date',
        'is_covered',
    ]
