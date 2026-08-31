from typing import Literal

ApiV1CredentialsDiscoverCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_CREDENTIALS_DISCOVER_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CredentialsDiscoverCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_credentials_discover_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1CredentialsDiscoverCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_CREDENTIALS_DISCOVER_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_DISCOVER_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
