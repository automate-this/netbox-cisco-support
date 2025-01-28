from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from netbox_cisco_support.models import CiscoDeviceTypeSupport, CiscoSupport

class CiscoDeviceTypeSupportSerializer(NetBoxModelSerializer):
    class Meta:
        model = CiscoDeviceTypeSupport
        fields = (
            'id',
            'device_type',
            'end_of_sale_date',
            'end_of_sw_maintenance_releases',
            'end_of_security_vul_support_date',
            'end_of_routine_failure_analysis_date',
            'end_of_service_contract_renewal',
            'last_date_of_support',
            'end_of_svc_attach_date',
            'created',
            'last_updated',
        )


class CiscoSupportSerializer(NetBoxModelSerializer):
    class Meta:
        model = CiscoSupport
        fields = (
            'id',
            'device',
            'coverage_end_date',
            'warranty_end_date',
            'is_covered',
            'created',
            'last_updated',
        )
