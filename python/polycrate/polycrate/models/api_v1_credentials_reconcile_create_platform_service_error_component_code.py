from typing import Literal

ApiV1CredentialsReconcileCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_CREDENTIALS_RECONCILE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CredentialsReconcileCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_credentials_reconcile_create_platform_service_error_component_code(
    value: str,
) -> ApiV1CredentialsReconcileCreatePlatformServiceErrorComponentCode:
    if value in API_V1_CREDENTIALS_RECONCILE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_RECONCILE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
