from typing import Literal

ApiV1EndpointsReconcileCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_ENDPOINTS_RECONCILE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsReconcileCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_endpoints_reconcile_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1EndpointsReconcileCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
