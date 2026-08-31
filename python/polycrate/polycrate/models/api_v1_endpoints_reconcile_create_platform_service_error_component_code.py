from typing import Literal

ApiV1EndpointsReconcileCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_ENDPOINTS_RECONCILE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsReconcileCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_endpoints_reconcile_create_platform_service_error_component_code(
    value: str,
) -> ApiV1EndpointsReconcileCreatePlatformServiceErrorComponentCode:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
