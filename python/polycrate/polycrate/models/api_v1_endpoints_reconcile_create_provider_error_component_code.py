from typing import Literal

ApiV1EndpointsReconcileCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ENDPOINTS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsReconcileCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_endpoints_reconcile_create_provider_error_component_code(
    value: str,
) -> ApiV1EndpointsReconcileCreateProviderErrorComponentCode:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
