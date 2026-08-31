from typing import Literal

ApiV1EndpointsReconcileCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_ENDPOINTS_RECONCILE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsReconcileCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_endpoints_reconcile_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1EndpointsReconcileCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
