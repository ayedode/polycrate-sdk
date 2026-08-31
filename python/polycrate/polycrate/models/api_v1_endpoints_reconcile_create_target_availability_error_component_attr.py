from typing import Literal

ApiV1EndpointsReconcileCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_ENDPOINTS_RECONCILE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsReconcileCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_endpoints_reconcile_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1EndpointsReconcileCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
