from typing import Literal

ApiV1ProviderAccountsPartialUpdatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsPartialUpdatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_provider_accounts_partial_update_platform_service_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsPartialUpdatePlatformServiceErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
