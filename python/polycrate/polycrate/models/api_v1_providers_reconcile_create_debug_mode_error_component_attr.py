from typing import Literal

ApiV1ProvidersReconcileCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_PROVIDERS_RECONCILE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersReconcileCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_providers_reconcile_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1ProvidersReconcileCreateDebugModeErrorComponentAttr:
    if value in API_V1_PROVIDERS_RECONCILE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_RECONCILE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
