from typing import Literal

ApiV1CredentialsReconcileCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_CREDENTIALS_RECONCILE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CredentialsReconcileCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_credentials_reconcile_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1CredentialsReconcileCreateDebugModeErrorComponentCode:
    if value in API_V1_CREDENTIALS_RECONCILE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_RECONCILE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
