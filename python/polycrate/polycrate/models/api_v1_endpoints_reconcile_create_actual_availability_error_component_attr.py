from typing import Literal

ApiV1EndpointsReconcileCreateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_ENDPOINTS_RECONCILE_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsReconcileCreateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_endpoints_reconcile_create_actual_availability_error_component_attr(
    value: str,
) -> ApiV1EndpointsReconcileCreateActualAvailabilityErrorComponentAttr:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
