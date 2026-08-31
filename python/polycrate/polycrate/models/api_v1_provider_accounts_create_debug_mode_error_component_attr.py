from typing import Literal

ApiV1ProviderAccountsCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_PROVIDER_ACCOUNTS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_provider_accounts_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsCreateDebugModeErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
