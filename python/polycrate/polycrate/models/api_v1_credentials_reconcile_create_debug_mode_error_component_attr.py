from typing import Literal

ApiV1CredentialsReconcileCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_CREDENTIALS_RECONCILE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsReconcileCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_credentials_reconcile_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1CredentialsReconcileCreateDebugModeErrorComponentAttr:
    if value in API_V1_CREDENTIALS_RECONCILE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_RECONCILE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
