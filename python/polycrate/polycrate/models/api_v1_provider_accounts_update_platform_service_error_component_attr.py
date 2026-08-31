from typing import Literal

ApiV1ProviderAccountsUpdatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_PROVIDER_ACCOUNTS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsUpdatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_provider_accounts_update_platform_service_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsUpdatePlatformServiceErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
